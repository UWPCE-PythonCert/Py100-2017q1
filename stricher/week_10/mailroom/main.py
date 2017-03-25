#!/usr/local/bin/python3

# TODO: complete/update


def main():
    from HomeMenu import HomeMenu
    from sys import stdin, stdout

    print("Welcome to Mailroom")

    from Database import Database
    from BenchData import DonorsDBBenchData, DonationsDBBenchData
    from DonationsTable import DonationsTable
    from DonorsTable import DonorsTable

    db = Database(DonorsTable(DonorsDBBenchData().data),
                  DonationsTable(DonationsDBBenchData().data))

    menu = HomeMenu(db)
    menu.get_action_from_user_and_perform()


if __name__ == "__main__":
    main()
