'''Задания №1 Напишите класс, отвечающий за животное. Реализуйте в классе аттрибуты: количество лап, издаваемый звук, кличка.
Реализуйте в классе метод "издать звук". Количество лап и звук задается при инициализации и ограничено (ограничения придумайте сами).
Кличка даётся после инициализации. Создайте несколько объектов класса, например кошка, собака, птица и т.д.'''


class Animal:
    def __init__(self, nickname):
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> gav, myu, ku-ka-re-ku"
        self.nickname = nickname

    def makeasound(self, nickname):
        print("DOG")
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> Gav-Gav"
        self.nickname = nickname

    def makeasound_1(self, nickname):
        print("CAT")
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> Myu-Myu"
        self.nickname = nickname

    def makeasound_2(self, nickname):
        print("CROW")
        self._numberofpaws = "--> 2 paws"
        self._emittedsound = "--> Kar-Kar"
        self.nickname = nickname

    def makeasound_3(self, numberofpaws, emittedsound, nickname):
        print("COW")
        self._numberofpaws = numberofpaws
        self._emittedsound = emittedsound
        self.nickname = nickname

    def makeasound_4(self, nickname):
        print("PARROT")
        self.__numberofpaws = "--> 2 paws"
        self.__emittedsound = "--> aristarchus smart bird"
        self.nickname = nickname

animal = Animal("Simpsony")
print(animal._numberofpaws)
print(animal._emittedsound)
print(animal.nickname)

dog = Animal("Brain")
dog.makeasound("Brain")
print(dog._numberofpaws)
print(dog._emittedsound)
print(dog.nickname)

cat = Animal("Barsik")
cat.makeasound_1("Barsik")
print(cat._numberofpaws)
print(cat._emittedsound)
print(cat.nickname)

crow = Animal("Rous")
crow.makeasound_2("Rous")
print(crow._numberofpaws)
print(crow._emittedsound)
print(crow.nickname)

cow = Animal("Burenka")
cow.makeasound_3("--> 4 paws", "Mu-Mu", "Burenka")
print(cow._numberofpaws)
print(cow._emittedsound)
print(cow.nickname)

cow = Animal("Aristarch")
cow.makeasound_4("Aristarch")
print(cow.nickname)

''' Задание №3 Напишите декоратор, который бы сообщал время запуска и время завершения функции.'''

import time

def time_of_function(function):
    def start(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print("Start Time")
        print(time.perf_counter_ns() - start_time)
        print("Completion Time")
        print(time.perf_counter_ns() + start_time )
        return res
    return start

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("0", "0"))


'''Задание №3 Реализуйте в классе животное возможность получать всю информацию об объекте 
(все пользовательские атрибуты и методы) через метод __str__'''

class Animal:
    def __init__(self, nickname):
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> gav, myu, ku-ka-re-ku"
        self.nickname = nickname

    def makeasound(self, nickname):
        print("DOG")
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> Gav-Gav"
        self.nickname = nickname


    def makeasound_1(self, nickname):
        print("CAT")
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> Myu-Myu"
        self.nickname = nickname


    def makeasound_2(self, nickname):
        print("CROW")
        self._numberofpaws = "--> 2 paws"
        self._emittedsound = "--> Kar-Kar"
        self.nickname = nickname

    def makeasound_3(self, numberofpaws, emittedsound, nickname):
        print("COW")
        self._numberofpaws = numberofpaws
        self._emittedsound = emittedsound
        self.nickname = nickname

    def makeasound_4(self, nickname):
        print("PARROT")
        self._numberofpaws = "--> 2 paws"
        self._emittedsound = "--> aristarchus smart bird"
        self.nickname = nickname

    def __str__(self):
        return f"class Animal: {self._numberofpaws}, {self._emittedsound}, {self.nickname}"


nickname = Animal("Brain")
nickname.makeasound("--> Brain")
print(str(nickname))

nickname = Animal("Barsik")
nickname.makeasound_1("--> Barsik")
print(str(nickname))

nickname = Animal("Rous")
nickname.makeasound_2("--> Rous")
print(str(nickname))

nickname = Animal("Burenka")
nickname.makeasound_3("--> 4 paws", "--> Mu-Mu", "--> Burenka")
print(str(nickname))

nickname = Animal("Aristarch")
nickname.makeasound_4("--> Aristarch")
print(str(nickname))

"""Зробити базовий клас Animal, і віднаслідуйся від нього класами Cat та Dog. В Cat та Dog визначи характерну для них поведінку (звук)"""

class Animal:
    def __init__(self, nickname):
        self._numberofpaws = "--> 4 paws"
        self._emittedsound = "--> myu, gav"
        self.nickname = nickname

class Cat(Animal):
    def makeasound_1(self, nickname):
        print("CAT")
        self._numberofpaws = "--> 4 cat paws"
        self._emittedsound = "--> Myu-Myu"
        self.nickname = nickname

class Dog(Animal):
    def makeasound_2(self, nickname):
        print("DOG")
        self._numberofpaws = "--> 4 dog paws"
        self._emittedsound = "--> Gav-Gav"
        self.nickname = nickname

animal = Animal("Simpsony")
print(animal._numberofpaws)
print(animal._emittedsound)
print(animal.nickname)

cat = Cat("Barsik")
cat.makeasound_1("Barsik")
print(cat._numberofpaws)
print(cat._emittedsound)
print(cat.nickname)

dog = Dog("Brain")
dog.makeasound_2("Brain")
print(dog._numberofpaws)
print(dog._emittedsound)
print(dog.nickname)
