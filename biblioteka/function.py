def add_biblia(biblia, reader, book, date_start, date_end):
    for i in biblia:
        if i['book'].lower() == book.lower():
            return False
    biblia.append({
        "reader": reader,
        "book": book,
        "date_start": date_start,
        "date_end": date_end
    })
    return True