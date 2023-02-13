import turtle
#1
"""src = turtle.Turtle()
for i in range(4):
	src.right(30)
	for j in range(4):
		src.forward(100)
		src.left(90)
turtle.exitonclick()"""

#4
"""import turtle

turtle.color('white','blue')
turtle.speed(20)
turtle.begin_fill()
for i in range(4):
	turtle.forward(100)
	turtle.left(90)
turtle.end_fill()

turtle.right(90)
turtle.forward(100)

turtle.color('white','green')
turtle.begin_fill()
for i in range(1):
	turtle.circle(50)
turtle.end_fill()
turtle.right(180)
turtle.forward(250)

turtle.right(90)
turtle.color('white','yellow')
turtle.begin_fill()
for i in range(3):
	turtle.forward(100)
	turtle.left(120)
turtle.end_fill()
turtle.exitonclick()"""

#Структура данных

#list - список - tizim
#tuple - кортеж - kortej
#dictionary - словарь - sozlik
#set 		- множество - koplik

person_1 = 'Allayar'
person_2 = 'Alpamis'
person_3 = 'Sultan'

"""car = [person_1,person_2,person_3]
print(car, type(car), car[0])	"""

"""school_resident = []
print('В школе данный момент',len(school_resident),'учеников')

school_resident.append('Aziz')
print('К нам присоединился', school_resident)
print('В школе данный момент',len(school_resident),'учеников')

school_resident.append('Erkin')
print('К нам присоединился', school_resident)
print('В школе данный момент',len(school_resident),'учеников')

school_resident.insert(1,'Damir')
print('К нам присоединился', school_resident)
print('В школе данный момент',len(school_resident),'учеников')

school_resident.extend(['Ilyas','Aydos','Alpamis'])
print('К нам присоединился', school_resident)
print('В школе данный момент',len(school_resident),'учеников')

print('Директор решил отсортировать их по именам', sorted(school_resident))

school_resident.pop(0)
print('Директор решил забрать первого студента')
print('Они',school_resident)

school_resident.remove('Erkin')
print('Директор решил забрать первого студента')
print('Они',school_resident)"""

"""numbers = []
print(numbers)
for i in range(5):
	numbers.append(i)
print(numbers)
#print(len(numbers))

s = 0
for i in numbers:
	s += i
	print(i)
print(s)

s = 0
for i in range(len(numbers)):
	s += i
	print(i)
print(s)"""

"""import random
students = list() # []

for i in range(5):
	#n = int(input('n: '))
	n = random.randint(-100,100)
	students.append(n)

for i in range(len(students)):
	print(i,':',students[i])"""

import random
m = int(input('m: '))
n = int(input('n: '))
print(m,'x',n,'таблица')

m_table = list()
for i in range(m):
	n_table = list()
	for j in range(n):
		num = random.randint(0,10)
		n_table.append(num)
	m_table.append(n_table)

for i in range(len(m_table)):
	for j in range(len(n_table)):
		if i == j:
			m_table[i][j] = 'AAA'
		if i == 0 and j < 5:
			m_table[i][j] = 'BBB'

for i in m_table:
	print(i)
