# Домашнее задание 1 
# 1. получить все анкеты с age < 30
# 2. где  age > 30
# 3. Если нет фото отделить от всех в отдельный список

# applications = [
#     {"name": "A", "age": 40, "photo": None},
#     {"name": "B", "age": 30, "photo": "some_pic"},
#     {"name": "C", "age": 22, "phto": "some_pic"},
#     {"name": "D", "age": 65, "photo": "_pic"},
#     {"name": "E", "age": 60, "photo": "ome_pic"},
#     {"name": "M", "age": 85, "phoo": "soe_pic"},
#     {"name": "Z", "age": 11116, "photo": "some_pic"}
# ]

# age_more_30_list = []
# age_less_30_list = []
# incorrect_photo_list = []
# no_photo_list = []

# for app in applications:
#     if app["age"] > 30:
#         age_more_30_list.append(app)
#     if app["age"] <= 30:
#         age_less_30_list.append(app)
#     try:
#         if not app["photo"]:
#             no_photo_list.append(app)
#     except:
#         incorrect_photo_list.append(app)

# print(age_more_30_list)
# print(age_less_30_list)
# print(incorrect_photo_list)
# print(no_photo_list)


# Домашнее задание 2
# Дан список сторон прямоугольников. Найти площадь каждого прямоугольника

# lst = [(2,2.2), (3,4), ('666','6'), ('7', '8.1'), (9, '10.2')]

# i = 1
# for x,y in lst:
#     try:
#         fl_x = float(x)
#         fl_y = float(y)
#     except:
#         print(f'Ошибка в данных S{i}')
#         continue
#     print(f'S{i} = {fl_x * fl_y}')
#     i += 1


# Задача 1
# 1. Найти кол-во строк в списке 
# 2. Найти самую длинную строку
# 3. Найти кол-во пробелов

# lst = ["asj dhasd", "sdas das da sd asd as d", 1,2,"a sd", "   "]

# number_of_string = 0
# number_of_spaces = 0
# longest_string = ""

# for element in lst:
#     if type(element) == str:
#         number_of_string += 1 
#     if type(element) == str and len(element) >= len(longest_string):
#         longest_string = element
#     if type(element) == str:
#         for symbol in element:
#             if symbol == ' ':
#                 number_of_spaces += 1

# print(f'Количество строк в списке = {number_of_string}')
# print(f'Самая длинная строка - {longest_string}')
# print(f'Количество пробелов в списке - {number_of_spaces}')


# Задача 2
# Сумма всех чисел 

# k = 28340928374

# S1 = 0
# S2 = 0

# string_k = str(k)

# for el in string_k:
#     S1 += int(el)

# el = 0
# while el <= len(string_k):
#     S2 += int(el)
#     el += 1

# print(f'Через цикл for сумма равна {S1}')
# print(f'Через цикл while сумма равна {S1}')


# Задача 3
# Факториал числа

# num = 7

# f1 = 1
# f2 = 1

# for i in range(1, num+1):
#     f1 *= i

# i = 1

# while i <= num:
#     f2 *= i
#     i += 1

# print(f'Факториал числа через цикл for равен {f1}')
# print(f'Факториал числа через цикл while равен {f2}')


# Задача 4 
# Удалить вхождения элемента, если он встречается более n раз

# lst = [1,1,2,3,4,5,5,4,3,1,5,4]
# n = 2

# new_lst = []

# for element in lst:
#     if not lst.count(element) >= n:
#         new_lst.append(element)

# print(f'Новый список = {new_lst}')


# Задача 5
# Найти самое часто встречающееся слово в строке

# our_string = 'String will never be empty and you do not need to account for different data types and string that not stupid data type in python. That string.'
# our_string = our_string.replace('.','')
# our_string = our_string.lower()
# our_string = our_string.split(' ')

# often = 0
# most_often_word = ''

# for word in our_string:
#     if our_string.count(word) > often:
#         most_often_word = word
#         often = our_string.count(word)

# print(most_often_word)


# Задача 6
# Получить дату рождения:
# 1) проверить, является ли пользователь совершеннолетним
# 2) если не является, то посчитать, сколько осталось до совершеннолетия
# 3) если является, то посчитать период, сколько он уже совершеннолетний

# 1

# from datetime import datetime, date, time

# print('Enter your birthday in format XX.XX.XXXX')
# dateOfBirth = input()

# currentDay = datetime.now().day
# currentMonth = datetime.now().month
# currentYear = datetime.now().year

# try:
#     dateOfBirth = dateOfBirth.split('.')
    
#     dayOfBirth = int(dateOfBirth[0])
#     monthOfBirth = int(dateOfBirth[1])
#     yearOfBirth = int(dateOfBirth[2])
 
#     if (int(dayOfBirth) > 31) or (monthOfBirth > 12) or (yearOfBirth > currentYear):
#         print('Wrong data input. Enter your birthday again.')
#     elif (currentYear - yearOfBirth) > 18:
#         print('User is adult')
#     elif (currentYear - yearOfBirth) == 18 and (currentMonth > monthOfBirth):
#         print('User is adult')
#     elif (currentYear - yearOfBirth) == 18 and (currentMonth == monthOfBirth) and (currentDay > dayOfBirth):
#         print('User is adult')
#     else:
#         print('User is not adult')
# except:
#     print('Wrong data input. Enter your birthday again.')
    

# 2

# from datetime import datetime, date, time

# print('Enter your birthday in format XX.XX.XXXX')
# dateOfBirth = input()

# currentDay = datetime.now().day
# currentMonth = datetime.now().month
# currentYear = datetime.now().year

# try:
#     dateOfBirth = dateOfBirth.split('.')
    
#     dayOfBirth = int(dateOfBirth[0])
#     monthOfBirth = int(dateOfBirth[1])
#     yearOfBirth = int(dateOfBirth[2])
 
#     if (int(dayOfBirth) > 31) or (monthOfBirth > 12) or (yearOfBirth > currentYear):
#         print('Wrong data input. Enter your birthday again.')
#     elif (currentYear - yearOfBirth) > 18:
#         print(f'User is adult already {currentYear - yearOfBirth - 18} years')
#     elif (currentYear - yearOfBirth) == 18 and (currentMonth > monthOfBirth):
#         print(f'User is adult already {currentYear - yearOfBirth - 18} years')
#     elif (currentYear - yearOfBirth) == 18 and (currentMonth == monthOfBirth) and (currentDay > dayOfBirth):
#         print(f'User is adult already {currentYear - yearOfBirth - 18} years')
#     else:
#         print('User is not adult')
#         print(f'To adult remains {18 - currentYear + yearOfBirth} years')
# except:
#     print('Wrong data input. Enter your birthday again.')


# Excercise 7
# Найдите три ключа с самыми высокими значениями в словаре 

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# keys = sorted(my_dict, key=my_dict.get)
# keys = keys[-3:]

# print(keys)


# Excercise 8 
# дан номер банковской карточки 5465 7788 2131 6577 надо спрятать все кроме последних 4-х символов

# startNum = 5465778821316577

# strNum = str(startNum)

# print(f'{len(strNum[0:-4])*"*"}{strNum[-4:]}')


# Excercise 9 
# Найти индекс 3-его вхождения числа 3 в список

# lst = [1,2,3,3,3,3]

# index = 0
# c = 0

# for l in lst:
#     if l == 3:
#         c += 1
#         if c == 3:
#             break
#     index += 1
# print(index)