import enum
from typing import List as List_, Optional as Optional_
from sqlalchemy import (
    create_engine, Column as Column_, ForeignKey as ForeignKey_, Table as Table_, 
    Text as Text_, Boolean as Boolean_, String as String_, Date as Date_, 
    Time as Time_, DateTime as DateTime_, Float as Float_, Integer as Integer_, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped as Mapped_, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass

# Definitions of Enumerations
class Genre(enum.Enum):
    History = "History"
    Fantasy = "Fantasy"
    Philosophy = "Philosophy"
    Adventure = "Adventure"
    Cookbooks = "Cookbooks"
    Romance = "Romance"
    Thriller = "Thriller"
    Poetry = "Poetry"
    Technology = "Technology"
    Horror = "Horror"


# Tables definition for many-to-many relationships
books = Table_(
    "books",
    Base.metadata,
    Column_("books", ForeignKey_("book.id"), primary_key=True),
    Column_("library", ForeignKey_("library.id"), primary_key=True),
)
books_1 = Table_(
    "books_1",
    Base.metadata,
    Column_("books", ForeignKey_("book.id"), primary_key=True),
    Column_("authors", ForeignKey_("author.id"), primary_key=True),
)

# Tables definition
class Publisher(Base):
    __tablename__ = "publisher"
    id: Mapped_[int] = mapped_column(primary_key=True)
    name: Mapped_[str] = mapped_column(String_(100))
    address: Mapped_[str] = mapped_column(String_(100))
    telephone: Mapped_[str] = mapped_column(String_(100))

class Author(Base):
    __tablename__ = "author"
    id: Mapped_[int] = mapped_column(primary_key=True)
    birth: Mapped_[dt_date] = mapped_column(Date_)
    name: Mapped_[str] = mapped_column(String_(100))

class Library(Base):
    __tablename__ = "library"
    id: Mapped_[int] = mapped_column(primary_key=True)
    name: Mapped_[str] = mapped_column(String_(100))
    web_page: Mapped_[str] = mapped_column(String_(100))
    address: Mapped_[str] = mapped_column(String_(100))
    telephone: Mapped_[str] = mapped_column(String_(100))

class Book(Base):
    __tablename__ = "book"
    id: Mapped_[int] = mapped_column(primary_key=True)
    title: Mapped_[str] = mapped_column(String_(100))
    pages: Mapped_[int] = mapped_column(Integer_)
    stock: Mapped_[int] = mapped_column(Integer_)
    price: Mapped_[float] = mapped_column(Float_)
    release: Mapped_[dt_date] = mapped_column(Date_)
    genre: Mapped_[Genre] = mapped_column(Enum(Genre))
    publisher_id: Mapped_[int] = mapped_column(ForeignKey_("publisher.id"))


#--- Relationships of the publisher table
Publisher.book: Mapped_[List_["Book"]] = relationship("Book", back_populates="publisher", foreign_keys=[Book.publisher_id])

#--- Relationships of the author table
Author.books: Mapped_[List_["Book"]] = relationship("Book", secondary=books_1, back_populates="authors")

#--- Relationships of the library table
Library.books: Mapped_[List_["Book"]] = relationship("Book", secondary=books, back_populates="library")

#--- Relationships of the book table
Book.publisher: Mapped_["Publisher"] = relationship("Publisher", back_populates="book", foreign_keys=[Book.publisher_id])
Book.library: Mapped_[List_["Library"]] = relationship("Library", secondary=books, back_populates="books")
Book.authors: Mapped_[List_["Author"]] = relationship("Author", secondary=books_1, back_populates="books")

# Database connection
DATABASE_URL = "sqlite:///Library.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)