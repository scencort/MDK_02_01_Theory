def find_product(products, name):
    for prod in products:
        if prod['name'].lower() == name.lower():
            return prod
    return None

def add_product(products, name, price, year, qty):
    prod = find_product(products, name)
    if prod:
        prod['qty'] += qty
    else:
        products.append({
            'name': name,
            'price': price,
            'year': year,
            'qty': qty
        })

def move_product(products, name, qty):
    prod = find_product(products, name)
    if prod and prod['qty'] >= qty:
        prod['qty'] -= qty
        return True
    return False

def supply_product(products, name, qty):
    prod = find_product(products, name)
    if prod:
        prod['qty'] += qty
        return True
    return False