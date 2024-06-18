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
        print(f"{company['name']}, klienci: {company['customers']}")


def add_company(companies: list) -> None:
    company_name = input("Nazwa restauracji fast-food: ")
    company_users = input("ilosc klientow: ")
    new_company = {"Nazwa restauracji fast-food": company_name, "klienci": company_users}
    print(new_company)
    companies.append(new_company)


def delete_company(companies: list) -> None:
    company_name = input("Ktora restauracje fast-food usunac: ")
    for company in companies:
        if company['name'] == company_name:
            companies.remove(company)


def update_company(companies: list) -> None:
    company_name = input("ktora restauracje fast-food uaktualnic: ")
    for company in companies:
        if company['name'] == company_name:
            company['name'] = input("Restauracja fast-food: ")
            company['customers'] = input("ilosc klientow: ")
            companies.append(company)


def show_employees(employees_list: list[dict]) -> None:
    for employee in employees_list:
        print(f"Imie: {employee['name']}, Nazwisko: {employee['surname']}, Restauracja: {employee['restaurant']}")


def add_employee(employees: list) -> None:
    employee_name = input("Imie: ")
    employee_surname = input("Nazwisko: ")
    employee_restaurant = input("Restauracja: ")
    new_employees = {"Imie: ": employee_name, "Nazwisko: ": employee_surname, "restauracja: ": employee_restaurant}
    print(employees)
    employees.append(new_employees)

