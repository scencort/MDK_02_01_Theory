def print_products(products):
    print("Список товаров:")
    print("Назв\tЦена\tГод\tКол-во")
    for prod in products:
        print(f"{prod['name']}\t{prod['price']}\t{prod['year']}\t{prod['qty']}")

def print_low_stock(products, low_stock = 10):
    print(f"Товары с количеством меньше {low_stock}:")
    for prod in products:
        if prod['qty'] < low_stock:
            print(f"{prod['name']} ({prod['qty']})")