from business.goncourt import Goncourt
from daos.book_dao import BookDao


if __name__ == '__main__':
    # book_dao = BookDao()
    # books = book_dao.read_book_by_selection(1)
    # for book in books:
    #     print(book)
    # selected_books = [books[0], books[8], books[11], books[12]]
    #
    # book_dao.create_book_selection(2, selected_books)

    # book_dao.update_book_number_of_votes(books[0].id, 3)
    # book_dao.update_book_number_of_votes(books[0].id, 4)
    goncourt = Goncourt()
    goncourt.ask_user_profile()
    while not goncourt.end_program:
        print("")
        goncourt.ask_main_actions()

