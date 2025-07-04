from data import loading_products, save_products

def search_product (products, name):
    for producti in products:
        if producti['name'].lower() == name.lower():
            return producti
    return None

def add_product(products, name, price, year, quantity):
    product = search_product(products, name)
    if product:
        product['quantity'] += quantity
    else:
        products.append({
            "name": name,
            "price": int(price),
            "year": int(year),
            "quantity": int(quantity)
        })

def delete_product(products, name, quantity):
    product = search_product(products, name)
    if product and product['quantity'] > quantity:
        product['quantity'] -= quantity
        return True
    return False