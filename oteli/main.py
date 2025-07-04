from data import *
from function import *

filename = "data.txt"

def menu():
    print("ЗДАРОВА!")
    print("1 - Добавить бомжей поспать")
    print("2 - Показать всех бомжей ебаных")
    print("3 - Посчитать бабки с бомжей")
    print("0 - пойти нахуй погулять")


def main():
    data = load_data(filename)
    while True:
        menu()
        vibor = int(input("Введи че-нить уже:\n"))
        if vibor == 1:
            print("Пиши ебать\n")
            date_in = input("Бомж заехал:\n")
            date_out = input("Бомж уехал:\n")
            guest = input("Бомж:\n")
            nomer_type =input("Как жить будет:\n")
            nomer = int(input("Цифры:\n"))
            x = add_booking(data, date_in,date_out, guest, nomer_type, nomer)
            if x == -1:
                print("Занято нахуй\n")
            if x == 1:
                print("Бомж добавлен\n")
            save_data(filename, data)

        if vibor == 2:
            print("На!\n")
            show_list_bookings(data)
        if vibor == 3:
            r = calc_all_price(data)
            print(f"Вот столько нахуй: {r}")

        if vibor == 0:
            print("Пока нахуй сука\n")
            break
if __name__ == "__main__":
    main()