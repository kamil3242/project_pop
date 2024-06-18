from models.data import users, employee, company
from utils.crud import show_user, add_new_user, delete_user, edit_user

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