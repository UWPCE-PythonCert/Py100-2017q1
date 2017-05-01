#!/usr/local/bin/python3.6


def main():

    from HomeMenu import HomeMenu
    from BenchData import DatabaseBench

    print("Welcome to Mailroom")

    db = DatabaseBench.db

    menu = HomeMenu(db)
    menu.get_action_from_user_and_perform()

if __name__ == "__main__":
    main()
