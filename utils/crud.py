import folium
import requests
from bs4 import BeautifulSoup


def show_user(users_list: list[dict]) -> None:
    for user in users_list:
        print(f"Imie: {user['name']} Nazwisko: {user['surname']}, Restauracja: {user['restaurant']} {user['location']}")


def add_new_user(users: list) -> None:
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    restaurant = input("Restauracja: ")
    location = input("Location: ")
    new_user = {"name": name, "surname": surname, "restaurant": restaurant, "location": location}
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
            user["location"] = input("Location: ")
            print(users)
            users.append(user)


def show_company(companies_list: list[dict]) -> None:
    for company in companies_list:
        print(f"{company['name']}, klienci: {company['customers']}, location: {company['location']}")


def add_company(companies: list) -> None:
    company_name = input("Nazwa restauracji fast-food: ")
    company_users = input("ilosc klientow: ")
    company_location = input("lokalizacja: ")
    new_company = {"Nazwa restauracji fast-food": company_name, "klienci": company_users,
                   "lokalizacja": company_location}
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
            company['location'] = input("Lokalizacja: ")
            companies.append(company)


def show_employees(employees_list: list[dict]) -> None:
    for employee in employees_list:
        print(
            f"{employee['name']} {employee['surname']}, Restauracja: {employee['restaurant']}, lokalizacja: {employee['location']}")


def add_employee(employees: list) -> None:
    employee_name = input("Imie: ")
    employee_surname = input("Nazwisko: ")
    employee_restaurant = input("Restauracja: ")
    employee_location = input("Location: ")
    new_employees = {'name': employee_name, 'surname': employee_surname, 'restaurant': employee_restaurant,
                     'location': employee_location}
    employees.append(new_employees)


def delete_employee(employees: list) -> None:
    employee_name = input("Ktory pracownik: ")
    for employee in employees:
        if f"{employee['name']}" == employee_name:
            employees.remove(employee)


def update_employee(employees: list) -> None:
    employee_name = input("Ktory pracownik: ")
    for employee in employees:
        if f"{employee['name']}" == employee_name:
            employee['name'] = input("Imie: ")
            employee['surname'] = input("Nazwisko: ")
            employee['restaurant'] = input("Restauracja: ")
            employee['location'] = input("Lokalizacja: ")
            employees.append(employee)


def company_user(companies: list[dict], users: list[dict]) -> None:
    company_name = input("podaj nazwę resrauracji fast-food: ")
    for company in companies:
        if company_name == company['name']:
            for user in users:
                if user['restaurant'] == company_name:
                    print(f"{user['name']}")


def company_employess(companies: list[dict], employees: list[dict]) -> None:
    company_name = input("podaj nazwę resrauracji fast-food: ")
    for company in companies:
        if company_name == company['name']:
            for user in employees:
                if user['restaurant'] == company_name:
                    print(f"{user['name']}")


def map_users(users):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for user in users:
        url = (f"https://pl.wikipedia.org/wiki/{user['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{user['name']},\n{user['location']}",
                      icon=folium.Icon(color='grey')).add_to(map)

    map.save('models/map/map_companies.html')


def map_employees(employees):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for employee in employees:
        url = (f"https://pl.wikipedia.org/wiki/{employee['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{employee['name']},\n{employee['location']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save('models/map/map_companies.html')


def map_company(companies):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for company in companies:
        url = (f"https://pl.wikipedia.org/wiki/{company['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{company['name']},\n{company['location']}",
                      icon=folium.Icon(color='darkpurple')).add_to(map)

    map.save('models/map/map_companies.html')
