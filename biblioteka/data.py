import os

filename = os.path.join(os.path.dirname(__file__), "biblioteka.txt")

def loading_data(filename = "biblioteka.txt"):
    biblia = []
    with open(filename, encoding="utf-8") as file:
        next(file)
        for i in file:
            reader, book, date_start, date_end = i.strip().split(";")
            biblia.append({
                "reader": reader,
                "book": book,
                "date_start": date_start,
                "date_end": date_end
            })
    return biblia

def save_data(filename, biblia):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("reader;book;date_start;date_end\n")
        for i in biblia:
            file.write(f"{i['reader']};{i['book']};{i["date_start"]};{i['date_end']}\n")