"""#1
names = list()
print(names, len(names))

#2
names = ['2','3']
print(names)
"""
#3
"""name = []
name.append(5)
name.append(4)
name.append(3)
print(name)
name.append([6,7])
print(name)

numbers = list()
numbers.append(5)
print(numbers)
numbers.insert(0, '5')
print(numbers)"""

"""words = ['Hello']
words.extend(['Hi','Привет'])
print(words)"""

import random
numbers = list()
n = int(input('n: '))
score = 0

for i in range(n):
	numbers.append(random.randint(0,9))
print('Старый список:',numbers)

"""
	Добавляем и удаляем элементов одновременно
""" 

for i in range(len(numbers)):
	if len(numbers) == n:
		user = int(input('user: '))
		if user:
			score += 1
		numbers.append(user)
		numbers.pop(0)
		if score == 2:
			break				
	else:
		raise IndexError
print('Обновленный список',numbers)

#Удаляем дубликаты из списка
"""
print(list(set(numbers)))
if len(numbers) == 5:
	numbers_w = list()
	for i in range(len(numbers)):
		if numbers[i] not in numbers_w:
			numbers_w.append(numbers[i])
else:
	raise IndexError
print(numbers_w)"""


"""import random
numbers = list()
n = int(input('n: '))
for i in range(n):
	numbers.append(random.randint(0,9))
print('Старый список:',numbers)


sorted_numbers = sorted(numbers)
print('Отсортированный список', sorted_numbers)
new_list = []
for i in range(len(sorted_numbers)):
	if sorted_numbers.count(i) >= 2:
		new_list.append(sorted_numbers[i])
print('Новый список',new_list)

"""

#Convert str -> list

"""name = input('What is your name? ').split()
print(name, type(name))

names = [
	'Aziz',
	'Sultan',
	'Damir'
]
print(names, type(names))

new_name = ",".join(names)
print(new_name, type(new_name))"""

'''
# Sort -> Bubble sort
import random
numbers = list()
n = int(input('n: '))
for i in range(n):
	numbers.append(random.randint(-100,100))
print('Старый список:',numbers)

for i in range(len(numbers)): #10
	for j in range(len(numbers)-1): #9
		if numbers[j] > numbers[j+1]:
			c = numbers[j]
			numbers[j] = numbers[j+1]
			numbers[j+1] = c
print('Отсортированный список', numbers)

'''


