
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Authors(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    books = relationship('Books', back_populates='author')

class Books(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    title = Column(String)
    publication_year = Column(String)
    author = relationship('Authors', back_populates='books')
    sales = relationship('Sales', back_populates='books')


class Sales(Base):
    __tablename__ = 'sales'

    sales_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.book_id'))
    # quantity = db.Column(db.Integer)
    pay_date = Column(Date)
    books = relationship('Books', back_populates='sales')

from datetime import datetime
pay_date_str = '2025.01.13'
pay_date = datetime.strptime(pay_date_str, '%Y.%m.%d').date()


engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def fill_out():
    author_1 = Authors(first_name='Фёдор', last_name='Достоевский')
    author_2 = Authors(first_name='Лев', last_name='Толстой')

    book_1 = Books(title='Преступление и наказание', author=author_1)
    book_2 = Books(title='Война и мир', author=author_2)

    sales_1 = Sales(books=book_1, pay_date=pay_date)

    session.add_all([author_1, author_2, book_1, book_2, sales_1])
    session.commit()

def print_books():
    print("\nСписок книг:")
    books = session.query(Books).all()
    for book in books:
        print(f"Книга: {book.title}, ее автор: {book.author.first_name} {book.author.last_name} и год издания: {book.publication_year}")

    print("\nКниги, которые купили:")
    books_sales = session.query(Sales).filter(Sales.pay_date != None).all()
    for book_sales in books_sales:
        print(f"Книга: {book_sales.books.title}")


if __name__ == "__main__":
    fill_out()
    print_books()

