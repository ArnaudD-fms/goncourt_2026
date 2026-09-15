# -*- coding: utf-8 -*-

"""
Classe book
"""
from dataclasses import dataclass, field
from datetime import date
from models.author import Author
from models.publisher import Publisher
from utils.date_utils import date_fr


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
    number_of_votes: int | None = field(default=None, init=False)

    def __str__(self):
        s = f"\"{self.title}\" a été écrit pas {self.author} et publié par {self.publisher}"

        additional_infos = []

        if self.summary is not None:
            additional_infos.append(f"Résumé : {self.summary}")
        if self.publication_date is not None:
            additional_infos.append(f"Date de publication : {date_fr(self.publication_date)}")
        if self.number_of_pages is not None:
            additional_infos.append(f"Nombre de pages : {self.number_of_pages}")
        if self.isbn is not None:
            additional_infos.append(f"Numéro ISBN :{self.isbn}")
        if self.price is not None:
            additional_infos.append(f"Prix : {self.price}")

        if additional_infos:
            s += "\n - Informations supplémentaires : \n - " + "\n - ".join(additional_infos)

        return s
