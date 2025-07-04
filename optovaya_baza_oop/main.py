class Product: #класс товара
    def __init__(self, name, price, year, quantity): #инициализация товара
        self.name = name
        self.price = float(price)
        self.year = int(year)
        self.quantity = int(quantity)

    def __str__(self): #строковое представление товара
        return f"{self.name} - {self.price} руб. ({self.year}) x {self.quantity} шт."
    

class Sklad: #класс склада
    def __init__(self): #инициализация склада
        self.products = []

    def add_product(self, product): #добавление товара на склад
        self.products.append(product)

    def get_value(self): #подсчет общей стоимости
        return sum(product.price * product.quantity for product in self.products)
    
    def show_all(self): #вывод всех товаров
        print("СПИСОК ТОВАРОВ:")
        for product in self.products:
            print(product)
        print(f"\nОБЩАЯ СТОИМОСТЬ: {self.get_value()} руб.")


class Postavshik: #класс поставщика
    def __init__(self, name): #инициализация поставщика
        self.name = name

    def postav(self, product, sklad): #добавление товара на склад
        sklad.add_product(product)


class MainSystem: #главный класс системы
    def __init__(self):
        self.sklad = Sklad()
        self.postavshik = Postavshik("ИП Ванян Гор")

    def load_data(self, filename): #загрузка данных из файла
        with open(filename, 'r', encoding='utf-8') as file:
            for i in file:
                name, price, year, quantity = i.strip().split(';')
                product = Product(name, price, year, quantity)
                self.postavshik.postav(product, self.sklad)


if __name__ == "__main__":
    sistema = MainSystem()
    sistema.load_data("C:/Users/yaros/Desktop/my_college_repository/3_course_2_semestr/MDK_02_01_ekzamen/optovaya_baza_oop/product.txt")
    sistema.sklad.show_all()