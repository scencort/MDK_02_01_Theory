import os
import func

def menu():
    print("1. фиксация нарушения")
    print("2. заблокировать права")
    print("3. штрафы водителя")
    print("4. выход нахуй")

def main():
    while True:
        menu()
        vibor = int(input("введите цифру: "))

        if vibor == 1:
            number = input("номер введи: ")
            pdd = input("тип штрафа: ")
            shtraf = int(input("цена штрафа: "))
            func.add_pdd(number, pdd, shtraf)
        elif vibor == 2:
            number = input("номер введи: ")
            func.block_driver(number)
        elif vibor == 3:
            total_shtraf = func.total_shtraf()
            for number, summa in total_shtraf.items():
                print(f"водила {number}: всего штрафов на {summa} рублей")
        elif vibor == 4:
            print("давай пока нахуй")
            break
        else:
            print("пункта нет такого")

if __name__ == "__main__":
    main()