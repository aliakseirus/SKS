# Here we go. Let's start study again


# Integer numbers

'''x = 44
y = 25

print('x + y =', x + y)		
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)
print('x // y =', x // y)
print('x % y =', x % y)
print('-x =', -x)
print('abs(x) =', abs(x))
print('divmod(x,y) =', divmod(x,y))
print('x ** y =', x ** y)
print('pow(x, y) =', pow(x,y))'''


# Float numbers

'''x = 150
y = 25.65

print('x + y =', x + y)
print('abs(x - y) =', abs(x - y))
print('round(x + y) =', round(x + y))'''

# Number systems

'''x = 435

print('bin(x) =', bin(x))
print('hex(x) =', hex(x))
print('oct(x) =', oct(x))'''


# Strings

'''s1 = 'Leonid'
s2 = 'Leon'

print('s1 + s2 =', s1 + s2)
print('s1 * 3 =', s1 * 3)
print('len(s1) =', len(s1))

print('s1[0] =', s1[0])
print('s2[2] =', s2[2])
print('s1[-3] =', s1[-3])

s3 = 'My name is Aliaksei'

print('s3[4:14] =', s3[4:14])
print('s3[2:-2] =', s3[2:-2])
print('s3[:6] =', s3[:6])
print('s3[1:] =', s3[1:])
print('s3[:] =', s3[:])

print('s3[::-1] =', s3[::-1])
print('s3[4:23:2] =', s3[4:23:2])
print('s3[2::3] =', s3[2::3])

s4 = "  I'm interesting in engineering and programming  "

print('len(s4) =', len(s4))
print("index =", s4.find('an'))
print("index =", s4.rfind('rest'))
print("index =", s4.index('eer'))
print("replace() =", s4.replace('ing','GOAL'))
print('split() = ', s4.split('in'))
print('isdigit() =', s4.isdigit())
print('isalpha() =', s4.isalpha())
print('isalnum() =', s4.isalnum())
print('islower() =', s4.islower())
print('isupper() =', s4.isupper())
print('isspace() =', s4.isspace())
print('istitle() =', s4.istitle())
print('upper() =', s4.upper())
print('lower() =', s4.lower())
print('startswith() =', s4.startswith('g'))
print('endswith() =', s4.endswith('g'))
print('count() =', s4.count('i'))
print('lstrip() =', s4.lstrip())
print('rstrip() =', s4.rstrip())
print('title() =', s4.title())'''


# Lists

'''lst_1 = list('First')	# create list
lst_2 = ['d', 'fff', '23', 55, 55, 55] 

print('List 1 =', lst_1)
print('List 2 =', lst_2)

lst_1.append('OOO')
print('append =', lst_1)

lst_1.extend(lst_2)
print('extend =', lst_1)

lst_1.insert(3, 'B')
print('insert =', lst_1)

lst_1.remove('t')
print('remove =', lst_1)

lst_1.pop()
print('pop =', lst_1)

lst_1.pop(5)
print('pop[5] =', lst_1)

print('index =', lst_1.index('d'))
print('count =', lst_1.count(55))

lst_1.reverse()
print('reverse =', lst_1)

lst_3 = lst_1.copy()
print(id(lst_1))
print(id(lst_2))
print(id(lst_3))	# Not the same id

lst_1.clear()
print('clear =', lst_1)

print(lst_1)
print(lst_2)
print(lst_3)'''


# Tuples

'''lst = [1, 2, 3, 4, 5, 6]
tup = (1, 2, 3, 4, 5, 6)

print(lst.__sizeof__())
print(tup.__sizeof__())	# tuples takes less memory

tup_1 = tuple()                     # create tuple
print('tup_1 is a', type(tup_1))

tup_2 = ()                          # create tuple
print('tup_2 is a', type(tup_2))

tup_3 = ('f')                       # create string (not tuple!)
print('tup_3 is a', type(tup_3))

tup_4 = ('f',)                      # create tuple
print('tup_4 is a', type(tup_4))'''