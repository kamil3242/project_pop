def show_user(users_list: list[dict]) -> None:
    for user in users_list:
        print(f"Imie: {user['name']} Nazwisko: {user['surname']}, Restauracja: {user['restaurant']}")

def add_new_user(users: list) -> None:
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    restaurant = input("Restauracja: ")
    new_user = {"name": name, "surname": surname, "restaurant": restaurant}
    print(new_user)
    users.append(new_user)

def delete_user(users: list) -> None:
    user_name = input("Kogo usunac?: ")
    for user in users:
        if f"{user['name']}" == user_name:
            users.remove(user)

def edit_user(users: list) -> None:
    user_name = input("Kogo uaktualnic?: ")
    for user in users:
        if f"{user['name']}" == user_name:
            user["name"] = input("Imie: ")
            user["surname"] = input("Nazwisko: ")
            user["restaurant"] = input("Restauracja: ")
            print(users)
            users.append(user)

def show_company(companies_list: list[dict]) -> None:
    for company in companies_list:
        print(f"{company['name']} klienci: {company['number users']}")



def add_company(company: dict) -> None:
    company_name = input("Nazwa restauracji fast-food: ")
    company_users = input("ilosc klientow: ")
    new_company = {"name": company_name, "number users": company_users}
    print(new_company)
    company.update(new_company)