from typing import List

from daos.dao import Dao
from models.author import Author
from models.book import Book
from models.publisher import Publisher


class BookDao(Dao[Book]):
    def read_book_by_selection(self, selection_number: int) -> List[Book]:
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
                book.summary = record["bo_summary"]
                book.publication_date = record["bo_publication_date"]
                book.number_of_pages = record["bo_number_of_pages"]
                book.isbn = record["bo_isbn"]
                book.price = record["bo_price"]
                books.append(book)

            return books
