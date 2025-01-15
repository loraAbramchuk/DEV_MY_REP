"""
Управление системой аренды недвижимости
Цель занятия:
Студенты создадут систему управления арендой недвижимости с использованием SQLAlchemy ORM.
Они будут работать с моделями, связанными через сложные отношения,
реализуют запросы с агрегациями, и применят транзакции для обработки аренды.

Система должна поддерживать следующие сущности:

Пользователь (User):

Имя (name)
Электронная почта (email)
Список договоров аренды (связь с Lease)

Объект недвижимости (Property):
Адрес (address)
Тип недвижимости (residential/commercial)
Стоимость аренды (rent_price)

Договор аренды (Lease):
Дата начала (start_date)
Дата окончания (end_date)
Арендатор (User)
Объект недвижимости (Property)
Статус (активен/завершён)

Платёж (Payment):

Сумма (amount)
Дата платежа (payment_date)
Договор аренды (Lease)
Бизнес-правила:

Один пользователь может арендовать несколько объектов недвижимости,
но не более одного договора аренды на один объект в одно и то же время.
Договор аренды может быть активирован только после внесения первого платежа.
Если договор завершён, объект недвижимости снова становится доступным для аренды.
При удалении пользователя все его договоры и платежи также должны быть удалены.


ЗАДАЧА
Добавление данных:

Добавить пользователей, объекты недвижимости и договоры.
Бизнес-логика:

Реализовать функцию для внесения платежа по договору.
Реализовать логику завершения договора (статус "completed").
Сложные запросы:

Найти всех пользователей, которые не внесли ни одного платежа.
Вывести объекты недвижимости, которые были арендованы более 3 раз.
Транзакции:

Обеспечить атомарность операций при создании договора и внесении первого платежа.
Расширение:

Добавить сущность "Агент" и реализовать комиссию для агентов от суммы аренды.


Оф.документация
https://docs.sqlalchemy.org/en/20/orm/quickstart.html

"""

from sqlalchemy import Integer, String, Date, Boolean, ForeignKey, create_engine, Enum, Float, CheckConstraint, func
from sqlalchemy.dialects.postgresql.named_types import EnumGenerator
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.testing.schema import Column
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)

    leases = relationship('Lease', back_populates='user')

class Property(Base):
    __tablename__ = 'properties'

    property_id = Column(Integer, primary_key=True)
    address = Column(String)
    property_type = Column(Enum( 'Жилая', 'Коммерческая', default = 'Жилая',  name='property_type'))
    rent_price = Column(Float)

    leases = relationship('Lease', back_populates='property')

class Lease(Base):
    __tablename__ = 'leases'

    lease_id = Column(Integer, primary_key=True)
    start_date = Column(Date, default=datetime.now)
    end_date = Column(Date)
    status_lease = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    property_id = Column(Integer, ForeignKey('properties.property_id'))
    agent_id = Column(Integer, ForeignKey('agents.agent_id'))

    user = relationship('User', back_populates='leases')
    property = relationship('Property', back_populates='leases')
    payments = relationship('Payment', back_populates='lease')
    agent = relationship('Agent', back_populates='leases')

    __table_args__ = (
        CheckConstraint('end_date > start_date', name='valid_lease_dates'),
    )

class Payment(Base):
    __tablename__ = 'payments'

    Base_id = Column(Integer, primary_key=True)
    amount = Column(Float)
    payment_date = Column(Date, default=datetime.now)
    lease_id = Column(Integer, ForeignKey('leases.lease_id'))

    lease = relationship('Lease', back_populates='payments')

class Agent(Base):
    __tablename__ = 'agents'

    agent_id = Column(Integer, primary_key=True)
    agent_name = Column(String)
    commission_rate = Column(Float)

    leases = relationship('Lease', back_populates='agent')

engine = create_engine('sqlite:///library_new.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_user(user_name: str, user_email: str):
    new_user = User(user_name=user_name, user_email=user_email)
    session.add(new_user)
    session.commit()
    print(f"Пользователь {user_name} добавлен")

def delete_user(name: str):
    user = session.query(User).outerjoin(Lease).outerjoin(Payment).filter(User.user_name == name).first()
    session.delete(user)
    session.commit()
    print(f"Пользователь {user.user_name} удален")

def add_property(address: str, property_type: str, rent_price: float):
    new_property = Property(address=address, property_type=property_type, rent_price=rent_price)
    session.add(new_property)
    session.commit()
    print(f"Недвижимость по адресу {address} добавлена.")

def add_lease(user_id: int, property_id: int, amount: float, agent_id: int = None):
    try:
        with session.begin():
            new_lease = Lease(
                start_date=datetime.now(),
                end_date=datetime.now().replace(year=datetime.now().year + 1),
                status_lease=True,
                user_id=user_id,
                property_id=property_id,
                agent_id=agent_id
            )
            session.add(new_lease)
            session.flush()

            payment = Payment(
                amount=amount,
                lease_id=new_lease.lease_id
            )
            session.add(payment)

            if agent_id:
                agent = session.query(Agent).filter_by(agent_id=agent_id).one()
                commission = amount * agent.commission_rate
                print(f"Комиссия агента {agent.agent_name}: {commission:.2f}")

    except IntegrityError:
        session.rollback()
        print("Ошибка транзакции: Операция откатилась")

def make_payment(lease_id: int, amount: float):
    lease = session.query(Lease).filter_by(lease_id=lease_id, status_lease=True).first()
    if not lease:
        print("Активный договор аренды не найден.")
        return

    payment = Payment(amount=amount, payment_date=datetime.today(), lease=lease)
    session.add(payment)

    total_payments = sum(p.amount for p in lease.payments) + amount
    if total_payments >= lease.property.rent_price:
        lease.status_lease = False
        print(f"Договор аренды {lease.lease_id} завершён")

    session.commit()

def users_without_pay():
    users = session.query(User).outerjoin(Lease).outerjoin(Payment).filter(Payment.payment_id == None)
    return [user.user_name for user in users]

def three_rent():
    apartments = session.query(Property.address).join(Lease).group_by(Property.address).having(func.count(Lease.lease_id) > 3).all()
    return apartments

try:
    add_user("Ivan", "ivan@mail.ru")
    add_property("Prospekt Mira 10", "Коммерческая", 12000.0)
    add_lease(user_id=1, property_id=1, amount=6000.0, agent_id=None)

    add_user("Оксана", "oksana@mail.ru")
    add_property("Prospekt Pobeditelej 106", "Жилая", 18900.0)
    add_lease(user_id=2, property_id=2, amount=8000.0, agent_id=None)

    delete_user('Оксана')
except ValueError as e:
    print(f"Ошибка: {e}")




