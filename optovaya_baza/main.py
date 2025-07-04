import os

filename = os.path.join(os.path.dirname(__file__), "baza.txt")
print("Путь к файлу:", filename)
print("Файл существует?", os.path.isfile(filename))

import function
import otchet
import data

def menushka():
    print("1. найти продукт")
    print("2. добавить продукт")
    print("3. удалить продукт")
    print("4. вывести все продукты")
    print("5. давай пока нахуй")

def main():
    load = data.loading_products(filename)
    while True:
        menushka()
        vibor = int(input("введи цифру: "))

        if vibor == 1:
            name = input("введи товар: ")
            if function.search_product(load, name):
                print("товар найден\n")
        elif vibor == 2:
            name = input("введи товар: ")
            price = float(input("введи цену товара: "))
            year = int(input("введи год: "))
            quantity = int(input("введи количество товара: "))
            function.add_product(load, name, price, year, quantity)
        elif vibor == 3:
            name = input("введи товар: ")
            quantity = int(input("введи количество товара: "))
            function.delete_product(name, quantity)
        elif vibor == 4:
            otchet.print_products(load)
        elif vibor == 5:
            print("давай пока нахуй")
            break
        else:
            print("ты братан выбрал ебанину какую-то")
            

if __name__ == "__main__":
    main()
