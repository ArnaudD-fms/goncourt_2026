import unittest
from datetime import date

from daos.book_dao import BookDao
from models.book import Book


class TestBookDao(unittest.TestCase):
    def setUp(self):
        self.book_dao = BookDao()

    def test_read_book_by_selection(self):
        books = self.book_dao.read_book_by_selection(1)

        self.assertIsInstance(books, list)

        for book in books:
            self.assertIsInstance(book, Book)
            self.assertIsNotNone(book.id)

        self.assertEqual(books[0].title, "Minotaure")
        self.assertEqual(books[0].publication_date, date(2026, 8, 19))
        self.assertEqual(books[3].title, "Le fabuleux piano")
        self.assertIsNone(books[15].isbn)
