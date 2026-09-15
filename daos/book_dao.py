from typing import List

import pymysql

from daos.dao import Dao
from models.author import Author
from models.book import Book
from models.publisher import Publisher


class BookDao(Dao[Book]):

    def read_book_by_selection(self, selection_number: int) -> List[Book]:
        """
        Récupère les livres correspondant à une sélection

        :param selection_number: le numéro de la sélection dont on souhaite récupérer les livres
        :return: la liste des livres sélectionés
        """
        with Dao.connection.cursor() as cursor:
            sql = """
                SELECT * FROM go_book
                JOIN go_book_selection ON bs_id_book = bo_id_book
                JOIN go_selection ON se_id_selection = bs_id_selection
                JOIN go_author ON au_id_author = bo_id_author
                JOIN go_publisher ON pu_id_publisher = bo_id_publisher
                WHERE se_number = %s
            """
            cursor.execute(sql, (selection_number,))
            records = cursor.fetchall()

            books = []
            for record in records:
                author = Author(record["au_first_name"], record["au_last_name"])
                publisher = Publisher(record["pu_name"])

                book = Book(record["bo_title"], author, publisher)
                book.id = record["bo_id_book"]
                book.summary = record["bo_summary"]
                book.publication_date = record["bo_publication_date"]
                book.number_of_pages = record["bo_number_of_pages"]
                book.isbn = record["bo_isbn"]
                book.price = record["bo_price"]
                books.append(book)

            return books

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
                id_selection = cursor.fetchone()

                # Création la liste des association livre / sélection que l'on souhaite insérer en base
                values = ", ".join(
                    f"({book.id}, "
                    f"{id_selection["se_id_selection"]})"
                    for book in books
                )

                # Execution de la réquête en passant les valeurs préparées
                sql = f"""
                    INSERT INTO go_book_selection (bs_id_book, bs_id_selection) VALUES {values};
                """
                cursor.execute(sql, values)

            # TODO pour la review avec les formateurs :
            #  est-ce une bonne approche ? (SELECT sur la table selection depuis le dao de book)
            #  est-ce que ce code respecte les bonnes pratiques ?
            Dao.connection.commit()

        except pymysql.MySQLError as e:
            Dao.connection.rollback()
            print(f"Erreur SQL : {e}")
