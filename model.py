from datetime import datetime
from pydantic import BaseModel,Field ,field_validator
from uuid import uuid4
from enum import Enum
from typing import  Optional
import textwrap

class Genre(str,Enum):
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    MYSTERY = "Mystery"
    FANTASY = "Fantasy"
    SCIENCE_FICTION = "Science Fiction"
    ROMANCE = "Romance"
    HORROR = "Horror"
    THRILLER = "Thriller"
    HISTORICAL = "Historical"
    BIOGRAPHY = "Biography"
    POETRY = "Poetry"
    CLASSIC = "Classic"
    ADVENTURE = "Adventure"
    COMEDY = "Comedy"
    DRAMA = "Drama"
    AUTOBIO = "Autobiography"
    EDUCAT = "Education"


class Book(BaseModel) :

    id : str = Field(default_factory=lambda:str(uuid4()))

    book_title: str = Field(
                    min_length=1,
                    max_length=50,
                    title="Book Name", 
                    description="The title of the book."
                    )
    
    author: str = Field(
                    min_length=2,
                    max_length=32,
                    title="Author Name",
                    description="The author of the book."
                    )
    
    summary: str = Field(
                        min_length=20,
                        max_length=500,
                        title="Book Summary", 
                        description="A brief summary of the book's content."
                        )
    
    description: Optional[str] = Field(
                                    min_length=20,
                                    max_length=1000,
                                    title="Book Description",
                                    description="A detailed description of the book, including its themes, plot, and key features."
                                    )
    
    release_date: str = Field(
                            title="Release Date", 
                            description="The date when the book was released, formatted as 'dd-mm-yyyy'."
                            )
    
    publisher: str = Field(
                        min_length=2,
                        max_length=32,
                        title="Publisher Name", 
                        description="The publisher of the book."
                        )
    
    genre: Genre = Field(
                        title="Book Genre", 
                        description="The genre or category of the book."
                        )

    @field_validator("release_date")
    @classmethod
    def validate_release_date(cls, value : str):
        try :
            datetime.strptime(value, "%d-%m-%Y")
            return value
        except ValueError :
            raise ValueError("Invalid date format, should be 'dd-mm-yyyy'")

    def __str__(self) -> str:
        return f"Book(book_title={self.book_title},author={self.author},genre={self.genre.value})"
    
    def __repr__(self) -> str:
        return textwrap.dedent(f"""
            Book(
            id={self.id},
            book_title={self.book_title},
            author={self.author},
            description={self.description},
            genre={self.genre.value}
            )
        """).strip()

    def model_dump(self):
        return {
            'id': self.id,
            'book_title': self.book_title,
            'author': self.author,
            'genre': self.genre.value,
            'release_date': self.release_date,
            'summary': self.summary
        }
    
    def model_dump_detail(self) :
        return {
            'id': self.id,
            'book_title': self.book_title,
            'author': self.author,
            'genre': self.genre.value,
            'release_date': self.release_date,
            'publisher': self.publisher,
            'summary': self.summary,
            'description':self.description
        }


    class Config:
        extra = "forbid"
        json_schema_extra =  {
            "example": {
                    "book_title": "The Great Gatsby",
                    "author": "F. Scott Fitzgerald",
                    "genre": "Fiction",
                    "release_date": "10-04-1925",  
                    "publisher": "Scribner",
                    "summary": "A novel set in the Roaring Twenties that tells the story of the enigmatic Jay Gatsby and his pursuit of wealth and love.",
                    "description": "The Great Gatsby, published in 1925, is a classic of American literature. It explores themes of wealth, love, and the American Dream ...",
            }
        }



