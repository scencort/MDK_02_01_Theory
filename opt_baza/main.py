import os

FILENAME = os.path.join(os.path.dirname(__file__), "product.txt")
print("Путь к файлу:", FILENAME)
print("Файл существует?", os.path.isfile(FILENAME))

import data
import logic
import report

filename = "product.txt"

def main():
    products = data.load_products(FILENAME)
    while True:
        print("\n1. Показать товары\n2. Отгрузить товар\n3. Поступление товара\n4. Добавить новый товар\n5. Отчёт по остаткам\n0. Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            report.print_products(products)
        elif choice == "2":
            name = input("Название товара: ")
            qty = int(input("Сколько отгрузить? "))
            if logic.move_product(products, name, qty):
                print("Отгружено.")
            else:
                print("Недостаточно товара!")
        elif choice == "3":
            name = input("Название товара: ")
            qty = int(input("Сколько поступило? "))
            if logic.supply_product(products, name, qty):
                print("Добавлено.")
            else:
                print("Такого товара нет.")
        elif choice == "4":
            name = input("Название: ")
            price = float(input("Цена: "))
            year = int(input("Год выпуска: "))
            qty = int(input("Количество: "))
            logic.add_product(products, name, price, year, qty)
            print("Товар добавлен.")
        elif choice == "5":
            threshold = int(input("Порог по остатку: "))
            report.print_low_stock(products, threshold)
        elif choice == "0":
            data.save_products(filename, products)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()