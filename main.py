from models.data import customer
from utils.crud import show_custmer

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
    print("witaj użytkowniku")
    while True:
        print("Menu:")
        break
