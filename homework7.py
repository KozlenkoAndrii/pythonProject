# 1  функция, которая заставит пользователя ввести целое число

def number_input(tp, message=None):
    tp_name = str(tp).split("'")[1]

    # if tp not in (int, float):
    #     raise TypeError(f'Unexpected type ({tp_name})')

    while True:
        try:
            return tp(input(f'{message} ({tp_name}) '))
        except Exception as e:
            print(f'Looser ! (Its not {message} )')


a = number_input(int, 'Enter lower border')

b = number_input(int, 'Enter upper border')


def y_n_question(msg=None):
    while True:
        answer = input(msg + ' (Y/N)')
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            return False
        else:
            print('Dont understand')


if y_n_question('Question'):
    print('I do')
else:
    print('NO')


# 2  дан список натуральных чисел в диапазоне от x до y, вывести все, кратные 3

def multiples(x, y):

    return [i for i in range(x, y) if not i % 3]


print(multiples(3, 500))


# 3 дан словарь {'a': 100, 'b': 100500, 'c':42, 'd': 99} - функция должна вернуть три самых больших значения

def slovar():

    d = {
        'a': 100,
        'b': 100500,
        'c': 42,
        'd': 99
    }

    print(sorted(d.values())[-3:])

slovar()

