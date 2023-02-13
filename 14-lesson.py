#2
"""user = input('Enter: ').lower() #str
print(user)
symbol = input('Enter new word: ').lower()
user = user.replace(user[0], symbol)
print('New text is',user)
"""

#10
"""s = 0
for i in range(1,50):
	if i % 4 == 0 and i % 6 == 0:
		print(i, end=' ')
		s += i
print('Итог:',s)"""

#while

"""for i in range(3):
	print(i)

print('--------------')

i = 0.5
while i < 3:
	print(i)
	i += 1

i = 0
while True:
	print(i)
	i += 1"""

#CTRL + C -> Отладка/Токтатыу

#1-2-3
"""start = 0
stop  = int(input('n: '))
while start <= stop:
	print(start)
	start += 1"""

#3
"""start = 0
stop  = 20
while start <= stop:
	if start % 2 == 0:
		print(start)
	start += 1"""

#break, continue -> Токтатыу, дауам етиу

"""for i in range(0,30):
	if i > 5 and i <= 10:
		continue
	if i == 25:
		break 
	print(i, end=' ')"""

"""s = 0
for i in range(5,41):
	if i % 5 == 0 and i % 2 == 0:
		if i == 30:
			break
		print(i, end=' ')
		s += i
print('\nКосынды:',s)"""

"""start = 10
stop  = 100
s = 0
while start <= stop:
	if start <= 50:
		if start % 3 == 0:
			print(start, end=' ')
			s += start
	start += 1
print('\nСумма:',s)"""

import datetime
i = 0
before = datetime.datetime.now()
while i < 20000:
	if i == 10000:
		break
	print(i)
	print('До: ',before) 
	after = datetime.datetime.now()
	i += 1
print('Потрачено: ',after)