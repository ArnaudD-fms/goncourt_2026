from typing import List

import pymysql

from daos.dao import Dao
from models.author import Author
from models.book import Book
from models.main_character import MainCharacter
from models.publisher import Publisher


class BookDao(Dao[Book]):

    def read_book_by_selection(self, selection_number: int) -> List[Book] | None:
        """
        Récupère les livres correspondant à une sélection

        :param selection_number: le numéro de la sélection dont on souhaite récupérer les livres
        :return: la liste des livres sélectionés
        """
        try:
            with Dao.connection.cursor() as cursor:
                # La requête récupère tous les livres liés à la sélection ainsi que les infos de l'auteur et l'éditeur.
                # Elle récupère également la liste des personnages principaux via une fonction d'agrégation.
                # TODO pour la review avec les formateurs :
                #   Requête trop complexe ? dois-je mieux décomposer le besoin ?
                sql = """
                    SELECT
                        go_book.*,
                        go_author.*,
                        go_publisher.*,
                        GROUP_CONCAT(mc_name SEPARATOR '|') AS main_characters
                    FROM go_book
                    JOIN go_book_selection ON bs_id_book = bo_id_book
                    JOIN go_selection ON se_id_selection = bs_id_selection
                    JOIN go_author ON au_id_author = bo_id_author
                    JOIN go_publisher ON pu_id_publisher = bo_id_publisher
                    LEFT JOIN go_main_character ON mc_id_book = bo_id_book
                    WHERE se_number = %s
                    GROUP BY bo_id_book
                """
                cursor.execute(sql, (selection_number,))
                records = cursor.fetchall()

                books = []
                # Construction de l'objet book
                for record in records:
                    # Instanciation de l'auteur et de l'éditeur
                    author = Author(record["au_first_name"], record["au_last_name"])
                    publisher = Publisher(record["pu_name"])

                    # Instanciation du livre
                    book = Book(record["bo_title"], author, publisher)
                    book.id = record["bo_id_book"]
                    book.summary = record["bo_summary"]
                    book.publication_date = record["bo_publication_date"]
                    book.number_of_pages = record["bo_number_of_pages"]
                    book.isbn = record["bo_isbn"]
                    book.price = record["bo_price"]

                    # Instanciation des personnages principaux récupérés via la fonction d'agégation
                    if record["main_characters"] is not None:
                        book.main_characters = [MainCharacter(name) for name in record["main_characters"].split("|")]

                    # Ajout du livre à la liste des livres
                    books.append(book)

                return books

        except pymysql.MySQLError as e:
            print(f"Erreur SQL : {e}")

    def create_book_selection(self, selection_number: int, books: List[Book]) -> None:
        """
        Créer en base les associations entre les livres et les sélections

        :param selection_number: le numéro de la sélection à laquelle on souhaite associer les livres
        :param books: la liste des livres à ajouter à la sélection
        """
        try:
            with Dao.connection.cursor() as cursor:
                # Récupération de l'id de la sélection depuis son numéro
                sql = """
                    SELECT se_id_selection FROM go_selection WHERE se_number = %s
                """
                cursor.execute(sql, (selection_number,))
                id_selection = cursor.fetchone()["se_id_selection"]

                # Création de la liste des associations à ajouter en base
                values = [
                    (book.id, id_selection)
                    for book in books
                ]

                sql = """
                    INSERT INTO go_book_selection
                    (bs_id_book, bs_id_selection)
                    VALUES (%s, %s)
                """
                cursor.executemany(sql, values)

            Dao.connection.commit()

        except pymysql.MySQLError as e:
            Dao.connection.rollback()
            print(f"Erreur SQL : {e}")

    def update_book_number_of_votes(self, id_book: int, number_of_votes) -> None:
        """
        Met à jour le nombre de votes d'un livre

        :param id_book: id du livre à modifier
        :param number_of_votes: nombre de votes que le livre a reçus
        """
        try:
            with Dao.connection.cursor() as cursor:
                sql = """
                    UPDATE go_book
                    SET bo_number_of_votes = bo_number_of_votes + %s
                    WHERE bo_id_book = %s
                """
                cursor.execute(sql, (number_of_votes, id_book))

            Dao.connection.commit()

        except pymysql.MySQLError as e:
            Dao.connection.rollback()
            print(f"Erreur SQL : {e}")

