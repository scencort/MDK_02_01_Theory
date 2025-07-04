def load_products(filename):
    products = []
    with open(filename, encoding="utf-8") as f:
        next(f)
        for line in f:
            name, price, year, qty = line.strip().split(";")
            products.append({
                "name": name,
                "price": float(price),
                "year": int(year),
                "qty": int(qty)
            })
    return products

def save_products(filename, products):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("название;цена;год;количество\n")
        for prod in products:
            f.write(f"{prod['name']};{prod['price']};{prod['year']};{prod['qty']}\n")