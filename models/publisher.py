# -*- coding: utf-8 -*-

"""
Classe publisher
"""
from dataclasses import dataclass, field


@dataclass
class Publisher:
    """
    Classe représentant un éditeur

    * id    : clé primaire de l'entité en base
    * name  : nom de l'éditeur
    """
    id: int | None = field(default=None, init=False)
    name: str

    def __str__(self):
        return self.name
