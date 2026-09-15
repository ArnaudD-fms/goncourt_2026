# -*- coding: utf-8 -*-

"""
Classe author
"""
from dataclasses import dataclass, field
from models.book import Book


@dataclass
class Author:
    id: int | None = field(default=None, init=False)
    first_name: str
    last_name: str
    biography: str = field(default=None, init=False)
    book: Book = field(default=None, init=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
