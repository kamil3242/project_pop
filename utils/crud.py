def show_custmer(customer_list: list[dict]) -> None:
    for customer in customer_list:
        print(f"Imie: {customer['name']} Nazwisko: {customer['surname']}, Restauracja: {customer['restaurant']}")