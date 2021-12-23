user_input = input('enter here: ')

user_input = user_input.strip()

res = ''

signs = '()- '

if ('@' in user_input) and ('.' in user_input):
    raw_list = user_input.split('@')
    # print(raw_list)

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

if res:
    print(f'\"{user_input}\" is {res}')
raw_list1 = user_input
if
if raw_list1.isalpha() and raw_list1[0].isupper and len(raw_list1) > 2:
    res = "Name"
else:
    print('WHAT?????')

# user_input = input('enter here: ')
#
# user_input = user_input.strip()
#
# res = ''  # переменная отвечающая за результат.
#
# signs = '()- '
#
# if ('@' in user_input) and ('.' in user_input):  # если собака в пользователе и точка в пользователе
#     raw_list = user_input.split('@') # мы разделяем по собаке
#     print(raw_list) #
#
#     if len(raw_list) != 2: # если длина не равно 2
#         pass    # то мы пропускаем
#     else:  # в противном случае
#         if raw_list[0].isalpha() and len(raw_list[0]) > 2: # если начало состоит из букв и длина больше 2
#             scnd_raw = raw_list[1].split('.')   # разделить по точке
#             if (scnd_raw[0].isalpha() and scnd_raw[1].isalpha()) and (len(scnd_raw[0]) > 2 and len(scnd_raw[1]) > 2):
#  # если scnd_raw[0].isalpha и scnd_raw[1].isalpha и длина scnd_raw[0] больше 2 и cnd_raw[0] больше 2
#                 res = 'Email' # то это Email
#
# else:  # в ином случае
#     raw_user_input = (user_input)
#
#     for letter in user_input: # для каждой буквы. что мы ввели от пользователя
#         if letter in signs:   # если буква содержит ()-" "
#             raw_user_input = raw_user_input.replace(letter, '') # то заменяем на ""
#     if any([
#         len(raw_user_input) == 13 and raw_user_input[0:3] == ["+", "3", "8", "0"] and raw_user_input[4:].isdigit(),
#         len(raw_user_input) == 10 and raw_user_input[0:2] == ["0", "6", "6"], ["0", "9", "9"], ["0", "5", "0"],
#         ["0", "9", "5"], ["0", "6", "3"], ["0", "9", "3"], ["0", "7", "3"], ["0", "6", "7"], ["0", "6", "8"],
#         ["0", "9", "6"], ["0", "9", "7"], ["0", "9", "8"], ["0", "3", "9"] and raw_user_input[3:].isdigit()
#     ]):
# # если длина = 13 и начало начинается с + и от 1 до конца у него цыфры
# # если длина = 10 и вся строка цифры
#         res = 'Phone' # то результат Phone
#
# if res:  # если есть результат и она не пустая
#     print(f'\"{user_input}\" is {res}')
# else:    # в ином случае
#     print('WHAT?????')  # Если введеная строка будет пустая будет False, и выведет WHAT?????