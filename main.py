




def login():
    print("logowanie")
    username = input("Nazwa użytkownika: ")
    password = input("Hasło: ")
    if username == "Kamil" and password == "geoinformatyka":
        print("zalogowano")
        return True
    else:
        print("nie zalogowano")
        return False


if __name__ == "__main__":
    print("witaj użytkowniku")
    while True:
        print("Menu:")
        break
        print("1. Login")