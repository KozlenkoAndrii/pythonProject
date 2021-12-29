''' Задание №1 Доделать, довести до ума, сделать красиво/просто/элегантно (нужное подчеркнуть) то, что делали на практике.
Копировать код с лекции не обязательно :р (Напоминаю условия: email - имя из букв длиной не менее 3 символов,
одна собака, доменное имя из двух частей через точку, обе части из букв длинной не менее 3 символов; телефон -
либо в формате +380121234567 либо 0121234567, дефисы, скобки пробелы - разрешены) '''

'''Задание №2 Добавить к проверке строки проверку на ФИО (Требования: длина не менее 2 символа для каждого слова,
              каждое слово с большой буквы, в слове только буквы, например Иванов Иван Иванович)'''

user_input = input('enter here: ')

user_input = user_input.strip()

res = ''

signs = '()- '

if ('@' in user_input) and ('.' in user_input):
    raw_list = user_input.split('@')

    if len(raw_list) != 2:
        pass
    else:
        if raw_list[0].isalpha() and len(raw_list[0]) > 2:
            scnd_raw = raw_list[1].split('.')
            if (scnd_raw[0].isalpha() and scnd_raw[1].isalpha()) and (len(scnd_raw[0]) > 2 and len(scnd_raw[1]) > 2):
                res = 'Email'

else:
    raw_user_input = user_input

    for letter in user_input:
        if letter in signs:
            raw_user_input = raw_user_input.replace(letter, '')
    if any([
        len(raw_user_input) == 13 and raw_user_input[0] == "+" and raw_user_input[1] == "3" and raw_user_input[2] == "8"
        and raw_user_input[3] == "0" and raw_user_input[4:].isdigit(),
        len(raw_user_input) == 10 and raw_user_input[0] == "0" and raw_user_input[1:].isdigit()
    ]):
        res = 'Phone'

    else:
        for raw_list1 in user_input.split():
            if raw_list1[0].isalpha() and raw_list1[0].isupper() and len(raw_list1) > 2:
                res = "Name"

if res:
    print(f'\"{user_input}\" is {res}')

else:
    print('WHAT?????')

''' Задание №3 Обеспечить пользователю возможность повторять операцию - спрашивать, хочет ли он продолжить (Y/N)...
               (вы уже делали такое в дз №3, задание 3, адаптируйте свой код под это) '''
# Мы в предыдущем задание расмотревали все варианты.

while True:
    operation = input("Хочешь ли ты повторить операцию? (Y/N): ")
    if operation == "Y":
        operation = operation
    else:
        if operation == "N":
            print("Программа завершина")
            break
        else:
            while True:
                if operation != "Y" and "N":
                    operation = input("Хочешь ли ты повторить операцию??? (Y/N): ")
                    while True:
                        operation = input("Хочешь ли ты повторить операцию?????? (Y/N): ")
                        if operation == "Y":
                            operation = operation
                        else:
                            if operation == "N":
                                print("Программа завершина")
                                break
                break
    break


while True:
    print('Do some actions')

    answer = None
    while True:
        operation = input("Хочешь ли ты повторить операцию? (Y/N): ")
        if operation not in 'YN':
            print('Wrong answer')
            continue
        answer = operation == 'Y'

    if not answer:
        break

''' Задание №4* Пользователь вводит несколько чисел через пробел. Определить все ли числа веденные пользователем 
                уникальны (нет ли среди чисел одинаковых по значению). Составить из уникальных чисел массив их квадратов.
                Составить из неуникальных чисел массив их кубов. '''


numbers = list(map(int, input("insert the number: ").split()))

for number in numbers:
    if numbers.count(number) == 1:
        print(number **2)
    if numbers.count(number) != 1:
        print(number **3)