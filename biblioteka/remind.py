import data

def print_date_end(biblia):
    vanyan = []
    for i in biblia:
        if i['date_end'] == '2025-07-03':
            vanyan.append(f"{i['reader']}")
    print(vanyan)
    return None