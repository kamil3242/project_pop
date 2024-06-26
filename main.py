from models.data import users, employees, companies
from utils.crud import (show_user, add_new_user, delete_user, edit_user,
                        show_company, add_company, delete_company, update_company,
                        show_employees, add_employee, delete_employee, update_employee,
                        company_user, company_employess, map_users, map_employees, map_company)


def login():
    print("logowanie")
    username = input("Nazwa użytkownika: ")
    password = input("Hasło: ")
    if username == "" and password == "":
        print("zalogowano")
        return True
    else:
        print("nie zalogowano")
        return False


if __name__ == "__main__":
    if login():
        while True:
            print("Menu:")
            print("1. opcje dla klientów")
            print("2. opcje dla praacownikow")
            print("3. opcje dla restauracji fast-food")
            print("4. mapa")

            menu_option: str = input("Menu:")
            if menu_option == "1":
                print("0. zakoncz program")
                print("1. Pokaż użytkownikow")
                print("2. dodaj nowego użytkownika")
                print("3. Usuń użytkownika")
                print("4. uaktualnij użytkownika")
                menu_option: str = input("Menu klientow: ")
                if menu_option == "0":
                    break
                if menu_option == "1":
                    show_user(users)
                if menu_option == "2":
                    add_new_user(users)
                if menu_option == "3":
                    delete_user(users)
                if menu_option == "4":
                    edit_user(users)
            if menu_option == "2":
                print("0. zakoncz program")
                print("1. Pokaz pracownika")
                print("2. dodaj pracownka")
                print("3. usun pracownika")
                print("4. uaktualnij pracownika")
                menu_option: str = input("Menu pracownikow: ")
                if menu_option == "0":
                    break
                if menu_option == "1":
                    show_employees(employees)
                if menu_option == "2":
                    add_employee(employees)
                if menu_option == "3":
                    delete_employee(employees)
                if menu_option == "4":
                    update_employee(employees)
            if menu_option == "3":
                print("0. zakoncz program")
                print("1. Pokaż restauracje fast-food")
                print("2. Dodaj nowe restauracje fast-food")
                print("3. usuń restauracje fast-food")
                print("4. uaktualnij restauracje fast-food")
                print("5. pokaz kilentow restauracji")
                print("6. pokaz pracownikow restauracji")
                menu_option: str = input("Menu restauracji: ")
                if menu_option == "0":
                    break
                if menu_option == "1":
                    show_company(companies)
                if menu_option == "2":
                    add_company(companies)
                if menu_option == "3":
                    delete_company(companies)
                if menu_option == "4":
                    update_company(companies)
                if menu_option == "5":
                    company_user(companies, users)
                if menu_option == "6":
                    company_employess(companies, employees)
            if menu_option == "4":
                print("0. zakoncz program")
                print("1. mapa klientow")
                print("2. mapa pracownikow")
                print("3. mapa restauracji")
                menu_option: str = input("Menu lokalizacji: ")
                if menu_option == "0":
                    break
                if menu_option == "1":
                    map_users(users)
                if menu_option == "2":
                    map_employees(employees)
                if menu_option == "3":
                    map_company(companies)
