# with open('settings.txt', 'r') as file:
#     for line in file.readlines():
#         item = line.split('=')
#         name = item[0]
#         value = item[1].replace('\n', '')
#         if name == 'DB_NAME':
#             DB_NAME = value
#         if name == 'DB_PASSWORD':
#             DB_PASSWORD = value
#         if name == 'DB_HOST':
#             DB_HOST = value
#         if name == 'DB_PORT':
#             DB_PORT = value

# DB_SETTINGS = {
#     'name': DB_NAME,
#     'password': DB_PASSWORD,
#     'host': DB_HOST,
#     'port': DB_PORT,
# }
# print("➡ DB_SETTINGS :", DB_SETTINGS)

# class DriveMixin:
#     # Mixin'ы содержат более-менее универсальные методы, 
#     # которые можно применить в множестве других классов, 
#     # например, ехать могут и машины, и тележки, и трактора.
#     def drive(self):
#         print('wroom')

# class Car(DriveMixin):
#     # Есть вообще у всех машин
#     wheels = 4 # Есть колеса
#     hood = True # Есть капот   
#     # ...
#     def __init__(
#         self, model, color,
#         mirrors,
#     ):
#         # Есть свои у каждой машины
#         # self - это сам автомобиль, в него может попасть как kia, так и tesla
#         self.model = model # модель авто
#         self.color = color + ' and blue' # цвет авто
#         self.mirrors = mirrors # зеркала(стекла) авто
    
    
#     def get_info(self):
#         # Все что угодно, от аттрибутов(переменных), до методов(функций), 
#         # можно получить через self
#         return '\n'.join((
#             f"Моя модель - {self.model}",
#             f"Иой цвет - {self.color}",
#             f"Мои зеркала - {self.mirrors}",
#         ))
    
#     # Перекраска
#     def recolor(self, new_color):
#         # Изменяем цвет через self
#         self.color = new_color
    
#     def change_mirrors(self, new_mirrors):
#         self.mirrors = new_mirrors
    
#     def update(self):
#         # Обращаемся к методам класса через self
#         self.change_mirrors('new_mirrors')
#         self.recolor('new_color')

# # Создаем объекты(экземпляры) класса
# kia = Car(
#     'Kia', 'white', 'toned')
# tesla = Car(
#     'Tesla', 'white', 'regular')
# bus = Car(
#     'Mercedes Sprinter', 'black', 'toned')

# # Достаем и изменяем информацию
# print(
#     "До перекраски\n",
#     bus.get_info()
# )

# bus.recolor('red')

# print(
#     "После перекраски\n",
#     bus.get_info()
# )


# # Трактор наследуется от машины, получая все ее методы и атрибуты
# class Tractor(Car):
#     def __init__(
#         self, model, color,
#         mirrors, horse_powers,
#         trailer=None # Можно использовать стандартные значения
#     ):
#         # super() обращается "чуть повыше", к родительскому классу
#         super().__init__(model, color, mirrors)
#         # Car запишет модель, цвет и стекла, все, что там не 
#         # предусмотрено, придется дописывать вручную
#         self.horse_powers = horse_powers
#         self.trailer = trailer
    
#     # Полиморфизм, метод с таким же названием есть в Car
#     def get_info(self):
#         old_info = super().get_info()
#         info = '\n'.join((
#             f"Мои лошадинные силы - {self.horse_powers}",
#             f"Мой прицеп - {self.trailer}"
#         ))
#         return f"{old_info}\n{info}"

# tractor = Tractor(
#     'Niva', 'red', 'regular',
#     35, trailer='chto-to s senom'
# )
# print(tractor.get_info())


# class Human:
#     # Рука - публичный атрибут, с ней можно проводить манипуляции, 
#     # не особо опасаясь за здоровье класса
#     hand = 'hand'

#     # Глаз - защищенный атрибут, он все еще на поверхности, 
#     # и с ним можно взаимодействовать, 
#     # но стоит быть осторожнее, иначе можно лишить класс части функционала (зрения)
#     _eye = 'eye'

#     # Сердце - приватный атрибут, его уже не так просто достать, и изменять его 
#     # крайне не рекомендуется, иначе можно полностью сломать класс
#     __heart = 'heart'


#     # Работа - публичный метод, многое можно поменять без вреда классу 
#     def job(self):
#         pass

#     # Дыхание - приватный метод, изменять его опасно, 
#     # если человек не сможет нормально дышать, то не сможет функционировать
#     def __breathe(self):
#         pass

# a = Human()
# a.hand
# a._eye
# # Приватные методы достаются немного по другому
# a._Human__heart


class Phonbook:
    def __init__(self, name, last_name, contact):
        self.name = name
        self.last_name = last_name
        self.contact = contact
    def get_info(self):
        info_ = '\n'.join((
            f"Имя - {self.name}",
            f"Фамилия - {self.last_name}",
            f"Контакт - {self.contact}",
    ))
        return f"{info_}"
    print(get_info("Иван", "Петров", "+996555777888"))