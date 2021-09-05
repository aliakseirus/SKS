# Homework 05.09.2021


# Excercise 1

start_list = [0,1,2, 'fjjefs',3,4,5,6, 'dddfa', 'dasfdgfwe', 'fff', 23, 13.7, '']

end_list = []

for symbol in start_list:
    if type(symbol) == str:
        end_list.append(start_list.index(symbol))

print('Answer of exercise 1:')
print('Index =', end_list)


# Excercise 2

start_list = [['fff,235', 42, 5324], 1, 'fff', 5, [2, 3, 'fgg'], 4, 'uuu', [5,6,7, 'wwetr', '5534']] 

end_list = []

for symbol in start_list:
    if type(symbol) == str:
        end_list.append(start_list.index(symbol))
    elif type(symbol) == list:
        for under_symbol in symbol:
            if type(under_symbol) == str:
                position = str(start_list.index(symbol)) + '-' + str(symbol.index(under_symbol))
                end_list.append(position)

print('Answer of exercise 2:')
print('Index =', end_list)