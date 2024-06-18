def show_custmer(customer_list: list[dict]) -> None:
    for customer in customer_list:
        print(f"Imie: {customer['name']} Nazwisko: {customer['surname']}, Restauracja: {customer['restaurant']}")

def add_new_customer(customer: list) -> None:
    name = input("Imie: ")
    surname = input("Nazwisko: ")
    restaurant = input("Restauracja: ")
    new_customer = {"name": name, "surname": surname, "restaurant": restaurant}
    print(new_customer)
    customer.append(new_customer)