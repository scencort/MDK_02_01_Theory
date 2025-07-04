import data

def add_pdd(number, pdd, shtraf):
    pdd = data.load_data()
    pdd.append([number, pdd, shtraf, 0])
    data.save_data(pdd)

def block_driver(number):
    pdd = data.load_data()
    for p in pdd:
        if p[0] == number:
            p[3] = 1
    data.save_data(pdd)

def total_shtraf():
    pdd = data.load_data()
    shtrafi = {}
    for p in pdd:
        if p[0] not in shtrafi:
            shtrafi[p[0]] = 0
        shtrafi[p[0]] += p[2]
    return shtrafi