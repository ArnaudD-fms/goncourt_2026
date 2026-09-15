
from daos.book_dao import BookDao


if __name__ == '__main__':
    book_dao = BookDao()
    books = book_dao.read_book_by_selection(1)
    selected_books = [books[0], books[8], books[11], books[12]]

    book_dao.create_book_selection(2, selected_books)

    ...

