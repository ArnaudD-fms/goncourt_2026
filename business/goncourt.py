from typing import ClassVar, List

from daos.book_dao import BookDao
from daos.jury_dao import JuryDao
from models.book import Book


class Goncourt:
    END_OF_PROGRAM_MESSAGE: ClassVar[str] = "Au revoir !"

    profile: str = "undefined"
    end_program: bool = False
    jury_dao = JuryDao()
    book_dao = BookDao()
    books: list[Book] = []

    def get_valid_input(self, max_choice: int, min_choice: int = 1):
        """
        Permet de vérifier si l'input saisi par l'utilisateur est valide

        :param max_choice: le choix max accepté dans les actions proposées
        :param min_choice: le choix min accepté dans les actions proposées
        :return: le choix de l'utilisateur sous forme d'int
        """
        valid_input = False
        user_input = ""
        invalid_input_message = f"Vous devez saison un nombre entre {min_choice} et {max_choice}"
        while not valid_input:
            user_input = input()
            if not user_input.isdigit():
                print(invalid_input_message)
                continue

            if not min_choice <= int(user_input) <= max_choice:
                print(invalid_input_message)
                continue

            valid_input = True

        return int(user_input)

    def ask_user_profile(self):
        """
        Demande à l'utilisateur de choisir son profil ou permet de quitter le programme

        """
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
        """
        Demande à l'utilisateur l'action qu'il souhaite effectuer en fonction de son profile

        """

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
                self.display_juries()

            case 2:
                self.display_books()

            case 3:
                if self.profile == "president":
                    self.update_selection()

                elif self.profile == "user":
                    self.end_program = True
                    print(self.END_OF_PROGRAM_MESSAGE)

            case 4:
                self.ask_to_vote()

            case 5:
                self.end_program = True
                print(self.END_OF_PROGRAM_MESSAGE)

    def update_selection(self):
        """
        Demande à l'utilisateur de mettre à jour les livres d'une sélection

        """

        # Récupère la sélection que l'utilisateur souhaite mettre à jour
        selection_to_update = self.ask_selection_to_update()

        # Récupère la liste des livres pouvant être choisi pour la sélection que l'utilisateur suhaite mettre à jour
        self.books = self.book_dao.read_book_by_selection(selection_to_update - 1)

        # Demande à l'utilisateur de choisir les livres qu'il souhaite ajouter à la sélection
        books_to_add: List[Book] = []
        continue_adding_book = True
        while continue_adding_book:
            self.ask_book_to_add(self.books, books_to_add)
            continue_adding_book = self.ask_continue_adding_books()

        # Appel du DAO afin de mettre à jour la sélection en base
        self.book_dao.create_book_selection(selection_to_update, books_to_add)
        print(f"Livres ajoutés à la sélection n° {selection_to_update} : ")
        for book in books_to_add:
            print(f" - {book.title}")

    def display_books(self):
        """ Récupère et affiche les livres d'une sélection """
        selection = self.ask_selection()
        books = self.book_dao.read_book_by_selection(selection)

        # TODO on pourrait aller vérifier la date dans l'objet Selection et la comparé à la
        #   date du jour, afin de ne pas afficher les sélections qui n'ont pas encore eu lieu
        if len(books) == 0:
            print("")
            print(f"La sélection n° {selection} n'a pas encore eu lieu.")

        for book in books:
            print("")
            print(book)

    def display_juries(self):
        """ Récupère et affiche les membres du jury """
        juries = self.jury_dao.read_all()
        for jury in juries:
            print(jury)

    # TODO redondance des méthode ask_selection et ask_selection_to_update > refcto nécessaire ?
    def ask_selection(self) -> int:
        """ Demande à l'utilisateur quelle sélection il souhaite afficher """
        print("")
        print("Quel sélection souhaitez vous afficher ? (1, 2 ou 3)")
        return self.get_valid_input(3)

    def ask_selection_to_update(self) -> int:
        """ Demande à l'utilisateur quelle sélection il souhaite mettre à jour """
        print("")
        print("Quel sélection voulez-vous mettre à jour ? (2 ou 3)")
        return self.get_valid_input(3, 2)

    def ask_book_to_add(self, books, books_to_add):
        # TODO l'algo fonctionne MAIS il faudrait vérifier s'il n'y a pas une solution plus optimisée.
        #   Il faudrait également vérifier les cas limite (pas eu le temps de tester en profondeur)
        """
        Affiche une liste de livre et demande à l'utilisateur de choisir le livre à ajouter à la liste des livres qui
        permettra de mettre à jour une sélection

        :param books: une liste de livre correspondante à une sélection
        :param books_to_add: la liste de livres permettant de mettre à jour une sélection
        """
        print("")
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
        """ Demande à l'utilisateur s'il souhaite ajouter d'autre livre à la sélection à mettre à jour"""
        print("")
        print("Voulez-vous ajouter d'autres livres à la sélection ? ")
        print(" 1 - Oui")
        print(" 2 - Non")

        user_action = self.get_valid_input(2)

        if user_action == 1:
            return True
        else:
            return False

    def ask_to_vote(self):
        # TODO (cf méthode ask_book_to_add) > même constat
        """
        Demande à l'utilisateur de choisir un livre parmi ceux couconrant dans la dernière sélection, et de choisir
        un nombre de votes à lui ajouter

        """
        books = self.book_dao.read_book_by_selection(3)

        if len(books) == 0:
            print("La dernère sélection n'a pas encore était établit. Le président doit sélectioner des livres avant"
                  "de pouvoir ajouter les votes.")

        else:
            print("pour quel livre souhaitez-vous ajouter des votes ?")

            for i, book in enumerate(books):
                print(f" - {i+1} : {book.title}")

            book_nbr = self.get_valid_input(len(books))

            print("Combien de votes souhaitez-vous ajouter ?")

            number_of_votes = self.get_valid_input(16)

            for i, book in enumerate(books):
                if book_nbr == i+1:
                    self.book_dao.update_book_number_of_votes(book.id, number_of_votes)
