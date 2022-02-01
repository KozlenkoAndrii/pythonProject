''' Задание №2 Пишем игру) Программа приветствует пользователя и просит задать диапазон чисел.
После ввода программа выбирает из введенного диапазано число и предлагает пользователю его угадать.
Если пользователь не угадал - предлагает пользователю угадать ещё раз пока пользователь её не угадает
Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить.'''

import random

def foo():
    game = input("Good day! Specify a range of numbers! In the format int-int: ")
    int_begin, int_end = map(int, game.split("-"))
    random_number = random.randint(int_begin, int_end)

    def foo1():
        while random_number != game:
            number = int(input("What number?: "))
            if number == random_number:
                operation = input("Хочешь ли ты повторить игру? (Y/N): ")
                if operation == "Y":
                    operation = operation
                else:
                    if operation == "N":
                        break
    foo1()
foo()

# ещё вариант

def foo():

    game = input("Good day! Specify a range of numbers! In the format int-int: ")
    int_begin, int_end = map(int, game.split("-"))

    random_number = random.randint(int_begin, int_end)

    def foo1():
        while random_number != game:
            number = int(input("What number?: "))
            if number == random_number:
                operation = input("Хочешь ли ты повторить игру? (Y/N): ")
                if not operation == "Y":
                    break
    foo1()
foo()

''' Задание №3 Добавить в задание №2 счетчик попыток. Кроме диапазона чисел пользователь вводит количество попыток, 
за которые он может угадать число. На каждом шаге сообщайте пользователю сколько попыток у него осталось. если 
пользователь не смог угадать за отведенное количество попыток сообщить ему об окончании (Looser!). Cпросить у 
пользователя, хочет ли он повторить игру (Y/N). Если Y повторить.'''


def foo():

    while True:

        game = input("Good day! Specify a range of numbers! In the format int-int : ")
        attempts = int(input("Enter the number of attempts: "))
        int_begin, int_end = map(int, game.split("-"))

        random_number = random.randint(int_begin, int_end)
        for i in range(attempts):
            number = int(input("What number?: "))
            attempts -= 1
            print("Попыток осталось", attempts)
            if number == random_number:
                print("Guessed!")
                break
        else:
            print("Looser!")
            print("Hidden number - {}".format(random_number))

            operation = input(f"Хочешь ли ты повторить игру? (Y/N): ")

            if operation not in ("Y"):
                print("Game over!")
                break
foo()