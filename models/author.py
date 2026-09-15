# -*- coding: utf-8 -*-

"""
Classe author
"""
from dataclasses import dataclass, field


@dataclass
class Author:
    id: int | None = field(default=None, init=False)
    first_name: str
    last_name: str
    biography: str
    # book: Book = field(default=None, init=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
