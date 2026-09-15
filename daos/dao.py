# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont hérite les classes de DAO de chaque entité
"""

from dataclasses import dataclass
from abc import ABC
from typing import ClassVar
import pymysql.cursors


@dataclass
class Dao[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='goncourt',
                        password='goncourtadmin',
                        database='goncourt',
                        cursorclass=pymysql.cursors.DictCursor)
