''' 1. Задание. Пользователь вводит строку. Преобразовать её в tuple сотоящий из слов.'''

user_input = input("Enter the string: " ).split()

user_input1 = tuple(user_input)

print(user_input1)

''' 2. Задание. Написать функцию, принимающую два аргумента. Если оба аргументв являются числами - вернуть их 
произведение, если строками - собрать в одну строку и вернуть, если первая строка, а вторая нет - вернуть словарь, 
 в котором ключ - первый аргумент, значение - второй.'''

def function(a, b):
    if type(a) == int and type(b) == int or type(a) == float and type(b) == float:
        return a * b
    elif type(a) == str and type(b) == str:
        return a + b
    elif type(a) == str and type(b) == float:
        slovary = {a: b}
        return slovary
    else:
        return "non-compliance by the condition of the task"


print(function(3.3, 3.3))
print(function("And", "rii"))
# print(function("my temperatura", 36.6))


# ещё пример с отдельными функциями

def foo(arg1, arg2):
    res = arg1 * arg2
    return float(res)


print(foo(5, 7))


def foo(arg3, arg4):
    res = arg3 + arg4
    return str(res)


print(foo("Kozl", "enko"))


def foo(arg5, arg6):
    res = {arg5: arg6}
    return str(arg5), int(arg6)


print(foo("Happy New Year", 2222))

''' 3. Задание. Дан словарь продавцов и цен на iphone xs max 256 gb у разных продавцов на hotline: 
{"citrus":47.999, "istudio":42.999, "moyo":49.999, "royal-service":37.245, "buy.ua":38.324, "g-store":37.166, 
"ipartner":38.988, "sota":37.720}, 
написать фукцию возвращающую список имен продавцов, чьи цены попадают в диапазон (from_price, to_price). '''

def list_of_seller_names(dictionary, a, b):
    return [dict_item[0] for dict_item in dictionary.items() if a <= dict_item[1] <= b]


iphone_dictionary = {"citrus": 47.999, "istudio": 42.999, "moyo": 49.999, "royal-service": 37.245, "buy.ua": 38.324,
                     "g-store": 37.166, "ipartner": 38.988, "sota": 37.720}

print(list_of_seller_names(iphone_dictionary, 37.000, 45.000))

''' 4. Задание. *Реализовать в виде функции ДЗ №3-3 (Попросить пользователя ввести с клавиатуры строку и вывести её на 
экран. Спросить у пользователя хочет ли он повторить операцию (Y/N)?. Повторять операцию если (Y), завершить выполнения 
если (N), если ответ не Y или N - переспрашивать пока не введет Y или N.) Получение ответа на вопрос (Y/N)? реализовать 
отдельной функцией и встроит в основную. '''


def play_operation():

    while True:
        operation = input("Хочешь ли ты повторить операцию? (Y/N): ")

        def play_operation1():

            if operation == "Y":
                print("Program continues")
            else:
                if operation == "N":
                    print("Program completed")
                else:
                    if operation != "Y" and "N":
                        print('Wrong answer')

        play_operation1()


play_operation()

# ещё вариант

def yes_or_no(operation):
    yes = ('Y', 'yes', 'Yes', 'y')
    no = ('N', 'no', 'n', 'no')

    while True:
        operation = input(f"Повторить операцию {operation}? (Y/N): ")

        if operation not in (*yes, *no):
            print("Wrong answer")
            continue

        return operation in yes


def play_operation():

    while True:
        print('Hello!')
        repeat = yes_or_no('Hello?')

        if not repeat:
            break

    print('The end')


play_operation()

''' 5. Задание. **Пользователь вводит строку произвольной длины. Функция должна вернуть словарь следующего содержания:
{
"0":количество пробелов в строке
"1":list слов из одной буквы
"2":list слов из двух букв
"3":list слов из трёх букв
...
punktuation:list уникальных знаков препинания
} '''


# иного вариана не получается придумать

def foo():
    world = 'python is the best. best programming software'
    words = world.split(' ')
    a = world.count(" ")
    b = world.count(".")
    longer = max(map(len, words))

    result = {}
    for i in range(longer):
        result[i] = []

    for word in words:
        result[len(word) - 1].append(word)
        result[(a)].append(" ")
        result[(b)].append(" . ")
    print(result)

foo()

# ещё вариант

def task5(raw_string):
    text_string = raw_string
    punctuation = '.,-!?():;'
    result = {
        0: text_string.count(' '),
        'punctuation': [],
    }

    for char in punctuation:
        if char in text_string:
            result['punctuation'].append(char)
            text_string = text_string.replace(char, '')

    word_list = text_string.split()

    for word in word_list:
        word_length = len(word)
        if word_length not in result:
            result[word_length] = [word]
        else:
            result[word_length].append(word)

    return result


res = task5('a !sdf asdf, qwert qwertyjkl zxc er erty wert r r yuu u asdf ,:')
print(res)
