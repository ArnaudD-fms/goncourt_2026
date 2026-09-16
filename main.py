from business.goncourt import Goncourt


if __name__ == '__main__':
    goncourt = Goncourt()
    goncourt.ask_user_profile()
    while not goncourt.end_program:
        print("")
        goncourt.ask_main_actions()
