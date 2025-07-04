def print_products(products):
    print("Список:")
    print("Название\tЦена\tГод\tКоличество")
    for producti in products:
        print(f"{producti['name']}\t{producti['price']}\t{producti['year']}\t{producti['quantity']}")