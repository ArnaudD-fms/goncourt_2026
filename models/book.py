# -*- coding: utf-8 -*-

"""
Classe book
"""
from dataclasses import dataclass, field
from datetime import date

from models.author import Author
from models.publisher import Publisher


@dataclass
class Book:
    """
    Classe représentant un livre

    * id                : clé primaire de l'entité en base
    * title             : titre du livre
    * summary           : résumé du livre
    * number_of_pages   : nombre de pages du livre
    * isbn              : numéro isbn du livre
    * price             : prix du livre
    """
    id: int | None = field(default=None, init=False)
    title: str
    author: Author
    publisher: Publisher
    summary: str | None = field(default=None, init=False)
    publication_date: date | None = field(default=None, init=False)
    number_of_pages: int | None = field(default=None, init=False)
    isbn: str | None = field(default=None, init=False)
    price: float | None = field(default=None, init=False)

    def __str__(self):
        # TODO: proposer un affichage en fonction des donnees disponibles
        return f"{self.title}"
