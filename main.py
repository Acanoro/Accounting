import datetime
from colorama import Fore, Style
from application.db.people import get_employees
from application.salary import calculate_salary


def main():
    print(Fore.BLUE + "Текущая дата:", datetime.datetime.now())
    print(Style.RESET_ALL)
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()
