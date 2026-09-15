# -*- coding: utf-8 -*-

"""
Classe main_character
"""
from dataclasses import dataclass, field


@dataclass
class MainCharacter:
    """
    Classe réprésentant un personnage principal d'un livre

    * id    : clé primaire de l'entité en base
    * name  : nom du personnage
    """
    id: int | None = field(default=None, init=False)
    name: str

    def __str__(self):
        return self.name
