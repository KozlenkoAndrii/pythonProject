'''Описать с помощью классов кухню. Реализовать наследованием классов мебель, приборы, посуду и т.д. с описанием свойств и методов'''

class Kitchen:
    def kitchen_method(self):
        print("Кухня")

class Mebel(Kitchen):
    def mebel_method(self):
        print("Кухонная мебель")

class Appliances(Kitchen):
    def appliances_method(self):
        print("Cтоловые приборы")

class Dishes(Kitchen):
    def dishes_method(self):
        print("Керамическая посуда")

class Technics(Kitchen):
    def technics_method(self):
        print("Бытовая техника")

class Plumbing(Kitchen):
    def plumbing_method(self):
        print("Сантехника")

class Lighting(Kitchen):
    def lighting_method(self):
        print("Освещение")

class Flowers(Kitchen):
    def flowers_method(self):
        print("Комнатные цветы")

mebel_a = Mebel()
mebel_a.kitchen_method()

technics_b = Technics()
technics_b.kitchen_method()

lighting_c = Lighting()
lighting_c.kitchen_method()

# ещё вариант

class Mebel:
    def mebel_method(self):
        print("Кухонная мебель")

class Appliances:
    def appliances_method(self):
        print("Cтоловые приборы")

class Dishes:
    def dishes_method(self):
        print("Керамическая посуда")

class Technics:
    def technics_method(self):
        print("Бытовая техника")

class Plumbing:
    def plumbing_method(self):
        print("Сантехника")

class Lighting:
    def lighting_method(self):
        print("Освещение")

class Flowers:
    def flowers_method(self):
        print("Комнатные цветы")

class Kitchen(Mebel, Appliances, Dishes, Technics, Plumbing, Lighting, Flowers):
    def kitchen_method(self):
        print("Кухня")

kitchen_a = Kitchen()
kitchen_a.mebel_method()
kitchen_a.appliances_method()
kitchen_a.dishes_method()
kitchen_a.technics_method()
kitchen_a.plumbing_method()
kitchen_a.lighting_method()
kitchen_a.flowers_method()
