#!/usr/local/bin/python3

#TODO: complete/update

def main():

    from HomeMenu import HomeMenu
    from sys import stdin, stdout
    from Signal import Signal

    print("Welcome to Mailroom")

    menu = HomeMenu()
    menu_signal = menu.get_action_from_user_and_perform(istream=stdin, ostream=stdout)
    program_signal = Signal()
    if menu_signal == program_signal.get_quit_program():
        from sys import exit
        exit(0)


if __name__ == "__main__" : main()