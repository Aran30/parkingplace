from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class Genre(Enum):
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

############################################
# Classes are defined here
############################################
class PublisherCreate(BaseModel):
    name: str
    address: str
    telephone: str
    book: Optional[List[int]] = None  # 1:N Relationship


class AuthorCreate(BaseModel):
    name: str
    birth: date
    books: Optional[List[int]] = None  # N:M Relationship (optional)


class LibraryCreate(BaseModel):
    web_page: str
    telephone: str
    name: str
    address: str
    books: Optional[List[int]] = None  # N:M Relationship (optional)


class BookCreate(BaseModel):
    release: date
    stock: int
    pages: int
    title: str
    price: float
    genre: Genre
    publisher: int  # N:1 Relationship (mandatory)
    library: List[int]  # N:M Relationship
    authors: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v

