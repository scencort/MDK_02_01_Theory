def add_booking(data, date_in, date_out, guest, nomer_type, nomer):
    for i in data:
        if i['room'] == nomer:
            return -1
    price = 0
    if nomer_type.lower() == 'люкс':
        price = 2500
    elif nomer_type.lower() == 'премиум':
        price = 2000
    else:
        price = 1400
    data.append({
        'date_in': date_in,
        'date_out': date_out,
        'guest': guest,
        'nomer_type': nomer_type,
        'room': nomer,
        'price': price
    })
    return 1

def show_list_bookings(data):
    for i in data:
        print(f"{i['date_in']} {i['date_out']} \n{i['guest']} {i['nomer_type']}\n {i['room']} {i['price']}\n")

def calc_all_price(data):
    sum = 0
    for i in data:
        sum += i['price']
    return  sum