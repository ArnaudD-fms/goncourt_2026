# -*- coding: utf-8 -*-

"""
Classe book
"""
from dataclasses import dataclass, field
from datetime import date


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
    summary: str
    publication_date: date
    number_of_pages: int
    isbn: str
    price: float

    def __str__(self):
        # TODO: proposer un affichage en fonction des donnees disponibles
        return f"{self.title}"
