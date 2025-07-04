import os

filename = os.path.join(os.path.dirname(__file__), "baza.txt")

def loading_products(filename):
    products = []
    with open(filename, encoding="utf-8") as file:
        next(file)
        for i in file:
            name, price, year, quantity = i.strip().split(";")
            products.append({
                "name": name,
                "price": int(price),
                "year": int(year),
                "quantity": int(quantity)
            })
    return products

def save_products(filename, products):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("name;price;year;quantity\n")
        for i in file:
            file.write(f"{i['name']};{i['price']};{i['year']};{i['quantity']}")