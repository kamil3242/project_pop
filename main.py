from models.data import users, employee, company
from utils.crud import show_user, add_new_user, delete_user, edit_user, show_company, add_company

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
login()

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
                print("Restauracje fast-food: ")
                show_company(company)
            if menu_option == "6":
                print("Dodaj restauracje fast-food: ")
                add_company(company)
            if menu_option == "8":
                print("Usun restauracje fast-food: ")

            if menu_option == "7":
                print("Uaktualnij restauracje fast-food: ")






