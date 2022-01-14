''' 1. Задание. Пользователь вводит строку. Преобразовать её в tuple сотоящий из слов.'''

user_input = input("Enter the string: " )

user_input1 = tuple(user_input)

print(user_input1)

''' 2. Задание. Написать функцию, принимающую два аргумента. Если оба аргументв являются числами - вернуть их 
произведение, если строками - собрать в одну строку и вернуть, если первая строка, а вторая нет - вернуть словарь, 
 в котором ключ - первый аргумент, значение - второй.'''

def function (a,b):
    if type(a)==int and type(b)==int:
        return (a*b)
    elif type(a)==str and type(b)==str:
        return (a+b)
    elif type(a)==str and type(b)==float:
        slovar={a:b}
        return slovar
    else:
        return "non-compliance by the condition of the task"
print(function(33,33))
print(function("And","rii"))
print(function("my temperatura", 36.6))

# ещё пример с отдельными функциями

def foo(arg1, arg2):
    res = arg1 * arg2
    return int(res)

print(foo(5, 7))

def foo(arg3, arg4):
    res = arg3 + arg4
    return str(res)

print(foo("Kozl", "enko"))

def foo(arg5, arg6):
    res = {arg5:arg6}
    return str(arg5), int(arg6)

print(foo("Happy New Year", 2222))

''' 3. Задание. Дан словарь продавцов и цен на iphone xs max 256 gb у разных продавцов на hotline: 
{"citrus":47.999, "istudio":42.999, "moyo":49.999, "royal-service":37.245, "buy.ua":38.324, "g-store":37.166, 
"ipartner":38.988, "sota":37.720}, 
написать фукцию возвращающую список имен продавцов, чьи цены попадают в диапазон (from_price, to_price). '''

def list_of_seller_names (dictionary, a, b):
    return [dict_item[0] for dict_item in dictionary.items() if a <= dict_item[1] <= b]

iphone_dictionary = {"citrus":47.999, "istudio":42.999, "moyo":49.999, "royal-service":37.245, "buy.ua":38.324,
"g-store":37.166, "ipartner":38.988, "sota":37.720}

print(list_of_seller_names (iphone_dictionary, 37.000, 45.000))

''' 4. Задание. *Реализовать в виде функции ДЗ №3-3 (Попросить пользователя ввести с клавиатуры строку и вывести её на 
экран. Спросить у пользователя хочет ли он повторить операцию (Y/N)?. Повторять операцию если (Y), завершить выполнения 
если (N), если ответ не Y или N - переспрашивать пока не введет Y или N.) Получение ответа на вопрос (Y/N)? реализовать 
отдельной функцией и встроит в основную. '''

def play_operation():
    def play_operation1():

        while True:
            operation = input("Хочешь ли ты повторить операцию? (Y/N): ")
            if operation == "Y":
                print("Program continues")
            else:
                if operation == "N":
                    print("Program completed")
                    break
                else:
                    if operation != "Y" and "N":
                        operation = input("Хочешь ли ты повторить операцию??? (Y/N): ")
    play_operation1()

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

# здесь немного не могу понять, как это всё правильно реализовать
# получилось сыровато

def foo():
    words = 'python is the best programming software'.split(' ')
    longer = max(map(len, words))

    result = {}
    for i in range(longer):
        result[i] = []

    for word in words:
        result[len(word) - 1].append(word)
    print(result)
foo()