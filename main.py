from models.data import users, employees, companies
from utils.crud import (show_user, add_new_user, delete_user, edit_user,
                        show_company, add_company, delete_company, update_company,
                        show_employees, add_employee, delete_employee, update_employee)


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
            print("1. Pokaż użytkownikow")
            print("2. dodaj nowego użytkownika")
            print("3. Usuń użytkownika")
            print("4. uaktualnij użytkownika")
            print("5. Pokaż restauracje fast-food")
            print("6. Dodaj nowe restauracje fast-food")
            print("7. usuń restauracje fast-food")
            print("8. uaktualnij restauracje fast-food")
            print("9. Pokaz pracownika")
            print("10. dodaj pracownka")
            print("11. usun pracownika")
            print("12. uaktualnij pracownika")



            menu_option: str = input("Menu:")
            if menu_option == "1":
                print("Użytownicy: ")
                show_user(users)
            if menu_option == "2":
                print("Dodaj użytkownika: ")
                add_new_user(users)
            if menu_option == "3":
                print("Kogo usunac: ")
                delete_user(users)
            if menu_option == "4":
                print("Kogo uaktualnic: ")
                edit_user(users)
            if menu_option == "5":
                print("Kogo restauracje fast-food: ")
                show_company(companies)
            if menu_option == "6":
                print("Dodaj restauracje fast-food: ")
                add_company(companies)
            if menu_option == "7":
                print("Usun restauracje fast-food: ")
                delete_company(companies)
            if menu_option == "8":
                print("uaktualnij restauracje fast-food: ")
                update_company(companies)
            if menu_option == "9":
                show_employees(employees)
            if menu_option == "10":
                add_employee(employees)
            if menu_option == "11":
                delete_employee(employees)
            if menu_option == "12":
                update_employee(employees)






