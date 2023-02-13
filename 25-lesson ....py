#1
"""countries = (
	'USA',
	'Russia',
	'Uzbekistan',
	'Karakalpakstan',
	'Kazakhstan'
)
print(f'Страны: {countries}')
user = int(input('Select: '))
print(f'Пользователь выбрал {countries[user]}')"""

"""#2
countries = (
	'USA',
	'Russia',
	'Uzbekistan',
	'Karakalpakstan',
	'Kazakhstan'
)
print(f'Страны: {countries}')
user = input('Select: ')
print(f'Пользователь выбрал {countries.index(user)}')"""

#3
"""sports = ['футбол','баскетбол']
print(sports)
user = input('Добавьте 1 вид спорта: ')

for i in range(len(sports)):
	if sports[i] == user:
		print('У нас есть такой вид спорта!')
		break
	if sports[i] != user:
		sports.append(user)
		break
print(f'Виды спорта: {sports}')"""

#4
"""lessons = [
	'math',
	'physics',
	'chemicals',
	'history',
	'geography',
	'biology'
]
student = input('I want to remove this lesson: ')
if student in lessons:
	lessons.remove(student)
for i in lessons:
	print(f'We have {i}')"""

#5
"""dishes = {
	1 : 'cocao',
	2 : 'plov',
	3 : 'beshbarmak',
	4 : 'pelmen',
	5 : 'manti'
}
for i,j in dishes.items():
	print('{} dish is {}'.format(j.capitalize()))

user = int(input('user: '))
if dishes.keys:
	dishes.pop(user)
for i,j in dishes.items():
	print(f'{i} dish is {j.capitalize()}')"""

"""#6
colors = [
	'black',
	'white',
	'orange',
	'yellow',
	'blue',
	'red',
	'green',
	'pink',
	'violet',
	'grey'
]
a = int(input('a: '))
b = int(input('b: '))

if (a >= 0 and a <= 4) and (b >= 5 and b <= 9):
	print(f'Colors {colors[a:b:1]}')
else:
	print('Error')"""

#Numeric arrays, Числовые массивы
import array
numbers = array.array('i', [])
print(array.typecodes)
for i in range(5):
	num = int(input('num: '))
	numbers.append(num)
print(f'Сумма: {sum(numbers)}')
numbers.reverse() #назад вперед
print(numbers) 
numbers.pop()
print(numbers)
print(f'Сколько раз повторяется число {numbers.count(5)}')
print(f'После сортировки {sorted(numbers)}')