# -*- coding: utf-8 -*-

"""
Classe author
"""
from dataclasses import dataclass, field
from models.book import Book


@dataclass
class Author:
    """
    Classe représenant l'auteur d'un livre
    * id            : clé primaire de l'entité en base
    * first_name    : prénom de l'auteur
    * last_name     : nom de l'auteur
    * biography     : biographie de l'auteur
    * book          : livre écrit par l'auteur
    """
    id: int | None = field(default=None, init=False)
    first_name: str
    last_name: str
    biography: str = field(default=None, init=False)
    book: Book = field(default=None, init=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
