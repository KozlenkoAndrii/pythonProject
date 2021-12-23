''' Задание №2 Пользователь вводит строку произвольной длины.
               Найти в строке самое длинное слово, в котром присутствует подряд две согласные буквы.
               Если в слове присутствует слово с тремя согласными буквами подряд - завершить выполнение.'''

import re

user_input = input("Enter the string: " )
if not re.search(r'(?i)[bcdfghjklmnpqpstvwxyz]{3}', user_input):
    print(max(re.findall(r'(?i)\w*[bcdfghjklmnpqpstvwxyz]{2}\w*', user_input), key=len))

# ещё вариант с русским текстом

import re

user_input = input("Введите строку: " )
if not re.search(r'(?i)[бвгджзйклмнпрстфхцчшщ]{3}', user_input):
    print(max(re.findall(r'(?i)\w*[бвгджзйклмнпрстфхцчшщ]{2}\w*', user_input), key=len))

''' Задание №3* Попросить пользователя ввести с клавиатуры строку и вывести её на экран.
                Спросить у пользователя хочет ли он повторить операцию (Y/N)?.
                Повторять операцию если (Y), завершить выполнения если (N), если ответ не Y или N - переспрашивать пока не введет Y или N. '''

while True:
    operation = input("Хочешь ли ты повторить операцию? (Y/N): ")
    if operation == "Y":
        operation = operation
    else:
        if operation == "N":
            print("Программа завершина")
            break
        else:
            if operation != "Y" and "N":
                 operation= input("Хочешь ли ты повторить операцию??? (Y/N): ")

# ещё вариант

def play_operation():

    while True:
        operation = input("Хочешь ли ты повторить операцию? (Y/N): ")
        if operation == "Y":
             operation = operation
        else:
            if operation == "N":
                print("Программа завершина")
                break
            else:
                if operation != "Y" and "N":
                    operation = input("Хочешь ли ты повторить операцию??? (Y/N): ")
play_operation()

# Следующая задача с предыдущего homework2, дополнительное задание с твои коментарием.
# я понимаю что ты хотел сделать в 97-110. но что будет если и второй раз он введет ерунду ? тут лучше цикл, выход из которого - првильно введенное число

''' Задание №5** Попросить пользователя ввести свой возраст.
    - если пользователю меньше 18 - вывести "мы не продаём агкоголь несовершеннолетним" 
    - если пользователю больше 70 - вывести "вам в пенсионный отдел"
    - в любом другом случае - вывести "добро пожаловать"
    - если пользователь ввел не число, спросить ещё раз. В случае повторного неправильного ввода - сказать ему что он не прав и завершить программу'''


while True:
    try:
        age = int(input("Введите свой возраст: "))
        if age < (18):
            print("мы не продаем алкоголь несовершеннолетним!")
            break
        elif age > (70):
            print("вам в пенсионный отдел!")
            break
        elif age > (17) and age < (71):
            print("добро пожаловать!")
            break
    except ValueError:
        try:
            age = int(input("Пожалуйста, повторно введите свой возраст: "))
        except ValueError:
            print("Вы не правы! Введите пожалуйста свой возраст ещё раз!: ")
