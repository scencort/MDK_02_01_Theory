def load_data(filename):
    data = []
    with open(filename, 'r', encoding="utf-8") as file:
        for i in file:
            date_in, date_out, guest, nomer_type, room, price = i.strip().split(";")
            data.append({
                'date_in': date_in,
                'date_out': date_out,
                'guest': guest,
                'nomer_type': nomer_type,
                'room': int(room),
                'price': int(price)
            })
    return data

def save_data(filename, data):
    with open(filename, 'w', encoding="utf-8") as f:
        for i in data:
            f.write(f"{i['date_in']};{i['date_out']};{i['guest']};{i['nomer_type']};{i['room']};{i['price']}\n")