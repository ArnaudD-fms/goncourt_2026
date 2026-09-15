# -*- coding: utf-8 -*-

"""
Classe book
"""
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Book:
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
