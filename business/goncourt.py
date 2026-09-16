from typing import ClassVar, List
from daos.book_dao import BookDao
from daos.jury_dao import JuryDao
from models.book import Book


class Goncourt:
    # Mettre en place un menu ou l'utilisateur pourra choisir l'action entrant le numero correspondant

    # Demander si on est utilisateur ou le president
    # si utilisateur choix 1 et 2 uniquement
    # si président tous les choix

    # 1 - Afficher la liste du jury
    # 2 - Afficher la liste des livres d'une selection
    #       2.1 - Demander la selection (entre 1 et 3) -> si date jour inferieur a date selection prevenir l'utilisateur
    # 3 - Indiquer les livres d'une selection
    #       3.1 - Demander la selection
    #       3.2 - Afficher les id des livres.
    #       3.3 - Demander d'entrer les id des livres à ajouter
    # 4 - Voter pour les livres
    #       4.1 Affiche directement les livres de la 3eme selection
    #       4.2 Demander de choisir un livre ne rentrant l'id
    #       4.3 Demander le nombre de votes à ajouter

    END_OF_PROGRAM_MESSAGE: ClassVar[str] = "Au revoir !"

    profile: str = "undefined"
    end_program: bool = False
    jury_dao = JuryDao()
    book_dao = BookDao()
    books: list[Book] = []

    def get_valid_input(self, max_choice: int, min_choice: int = 1):
        valid_input = False
        user_input = ""
        while not valid_input:
            user_input = input()
            if not user_input.isdigit():
                print("saisie incorrect")
                continue

            if not min_choice <= int(user_input) <= max_choice:
                print("saisie incorrect")
                continue

            valid_input = True

        return int(user_input)

    def ask_user_profile(self):
        print("Etes vous un simple utilisateur ou bien le GRAND et VENERABLE président de l'académie goncourt ?")
        print(" 1 - Simple utilisateur")
        print(" 2 - Vénérable président")
        print(" 3 - Quitter le programme")

        user_action = self.get_valid_input(3)

        match user_action:
            case 1:
                self.profile = "user"
            case 2:
                self.profile = "president"
            case 3:
                self.end_program = True
                print(self.END_OF_PROGRAM_MESSAGE)

    def ask_main_actions(self):

        user_action = 0

        print("Que souhaitez-vous faire ?")
        print(" 1 - Afficher le jury")
        print(" 2 - Afficher les livres d'une sélection")

        if self.profile == "president":
            print(" 3 - Indiquer les livres d'une Sélection")
            print(" 4 - Voter pour un livre")
            print(" 5 - Quitter le programme")
            user_action = self.get_valid_input(5)
        elif self.profile == "user":
            print(" 3 - Quitter le programme")
            user_action = self.get_valid_input(3)

        match user_action:

            case 1:
                juries = self.jury_dao.read_all()
                for jury in juries:
                    print(jury)

            case 2:
                selection = self.ask_selection()
                books = self.book_dao.read_book_by_selection(selection)
                for book in books:
                    print(book)

            case 3:
                if self.profile == "president":
                    selection_to_update = self.ask_selection_to_update()
                    self.books = self.book_dao.read_book_by_selection(selection_to_update-1)
                    books_to_add: List[Book] = []
                    continue_adding_book = True
                    while continue_adding_book:
                        self.ask_book_to_add(self.books, books_to_add)
                        continue_adding_book = self.ask_continue_adding_books()

                    self.book_dao.create_book_selection(selection_to_update, books_to_add)

                elif self.profile == "user":
                    self.end_program = True
                    print(self.END_OF_PROGRAM_MESSAGE)

            case 4:
                print("self.vote()")

            case 5:
                self.end_program = True
                print(self.END_OF_PROGRAM_MESSAGE)

    def ask_selection(self) -> int:
        print("Quel sélection souhaitez vous afficher ? (1, 2 ou 3)")
        return self.get_valid_input(3)

    def ask_selection_to_update(self) -> int:
        print("Quel sélection voulez-vous mettre à jour ? (2 ou 3)")
        return self.get_valid_input(3, 2)

    def ask_book_to_add(self, books, books_to_add):
        for i, book in enumerate(books):
            print(f" - {i+1} : {book.title}")

        print("Entrez le numéro du livre à ajouter à la sélection : ")
        book_nbr = self.get_valid_input(len(books))

        for i, book in enumerate(books):
            if book_nbr == i+1:
                if book not in books_to_add:
                    books_to_add.append(book)
                else:
                    print("Ce livre concourt déjà pour cette sélection")

    def ask_continue_adding_books(self):
        print("Voulez-vous ajouter d'autres livres à la sélection ? ")
        print(" 1 - Oui")
        print(" 2 - Non")

        user_action = self.get_valid_input(2)

        if user_action == 1:
            return True
        else:
            return False
