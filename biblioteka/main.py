import os

filename = os.path.join(os.path.dirname(__file__), "biblioteka.txt")
print("Путь к файлу:", filename)
print("Файл существует?", os.path.isfile(filename))

import data
import function
import remind

def menushka():
    print("1. добавить запись")
    print("2. вывести тех самых козлов")
    print("3. съебался нахуй")

def main():
    load = data.loading_data(filename)
    biblia = []
    while True:
        menushka()
        vibor = int(input("введи цифру тварина: "))

        if vibor == 1:
            reader = input("введи читателя сука ебаная: ")
            book = input("введи книгу шакал: ")
            date_start = input("введи дату, когда хочешь ты там чё-то начать: ")
            date_end = input("введи дату конца (Кирилл заканчивает за 45 секунд): ")
            function.add_biblia(load, reader, book, date_start, date_end)
            data.save_data(filename, load)
        elif vibor == 2:
            x = remind.print_date_end(load)
            if x:
                print(x)
        elif vibor == 3:
            print("съебался нахуй")
            break
        else:
            print("ты ебать какой пункт выбрал вообще, нет такого")
                
if __name__ == "__main__":
    main()