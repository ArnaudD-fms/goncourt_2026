# -*- coding: utf-8 -*-

"""
Classe selection
"""
from dataclasses import dataclass, field
from datetime import date

from utils.date_utils import date_fr


@dataclass
class Selection:
    """
    Classe représentant une étape de la sélection du prix Goncourt

    * id        : clé primaire de l'entité en base
    * number    : étape de la sélection
    * date      : date de début de la sélection
    """
    id: int | None = field(default=None, init=False)
    number: int
    date: date

    def __str__(self):
        return f"Sélection n°{str(self.number)} commencant à la date du {date_fr(self.date)}"
