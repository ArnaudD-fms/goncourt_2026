# -*- coding: utf-8 -*-

"""
Classe jury
"""

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Jury:
    """
    Jury de l'académie Goncourt
    * id                : clé primaire de l'entité en base
    * first_name        : prénom du jury
    * last_name         : nom du jury
    * joining_date      : date d'entrée à l'académie Goncourt
    * is_president      : indique s'il s'agit du président du jury
    """
    id: int | None = field(default=None, init=False)
    first_name: str
    last_name: str
    joining_date: date
    is_president: bool

    def __str__(self):
        s: str = f"{self.first_name} {self.last_name} à rejoint l'Académie Goncourt le {self.joining_date}."
        if self.is_president:
            s += " C'est également le président du jury."
        return s
