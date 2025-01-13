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
from sqlalchemy import Integer, String, Date, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.testing.schema import Column

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)
    # lease_id = Column(Integer, ForeignKey('leases.lease_id'))
    leases = relationship('Lease', back_populates='user')


class Property(Base):
    __tablename__ = 'properties'

    property_id = Column(Integer, primary_key=True)
    address = Column(String)
    residential = Column(String)
    rent_price = Column(Integer)
    leases = relationship('Lease', back_populates='property')


class Lease(Base):
    __tablename__ = 'leases'

    lease_id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    status_lease = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    property_id = Column(Integer, ForeignKey('properties.property_id'))
    user = relationship('User', back_populates='leases')
    property = relationship('Property', back_populates='leases')
    payments = relationship('Payment', back_populates='lease')


class Payment(Base):
    __tablename__ = 'payments'

    Base_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    payment_date = Column(Date)
    lease_id = Column(Integer, ForeignKey('leases.lease_id'))
    lease = relationship('Lease', back_populates='payments')



engine = create_engine('sqlite:///library_new.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_user():
    user_1 = User(user_name='Pavel', user_email='pavel@gmail.com')
    user_2 = User(user_name='Anton', user_email='anton@mail.ru')

    session.add_all([user_1, user_2])
    session.commit()


add_user()

users = session.query(User.user_name).all()
print(users)
