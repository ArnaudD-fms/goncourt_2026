from daos.book_dao import BookDao

if __name__ == '__main__':
    book_dao = BookDao()
    books = book_dao.read_book_by_selection(1)
    for book in books:
        print("")
        print(book)

    ...

