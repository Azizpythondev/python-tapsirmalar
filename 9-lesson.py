#1

"""name = 'gjksdfgjkdfjgdfjgkdfkgjdflgj'
print(len(name))
print(name[27])
print(name[len(name)-1])"""

#9
"""name = input('Enter: ')
if name.islower():
	if name[len(name)-1] == 'b':
		print('B')
	elif name[len(name)-1] == 'v':
		print('V')
	else:
		print('Error')
else:
	print(False)"""

#10
"""user = input('Enter: ').strip().lower()
#words = 'qwertyuiopasdfghjklzxcvbnm'
word = input('Enter a word: ')

if user.count(word) == 2:
	#текст -> qwerii -> weqrii
	#user[(len(user)-1)//2] -> середина -> e
	#user[0:((len(user)-1)//2)] -> до середины -> qw
	#user[((len(user)-1)//2)+1:len(user)] -> до края -> rii
	#user[0] -> первый элемент -> q
	user = user[1:((len(user))//2)] + user[0] + user[((len(user)-1)//2)+1:len(user)]
	print(user)
else:
	print('Error')"""

#Цикл -> Loop
#range(start,stop,step)

"""for index in range(1,100): 
	print(index)"""

"""name = int(input('enter: '))
for index in range(name):
	if index == 10:
		print('Erkinbay qalay!')
	if index == 14:
		print(True)
	print(index, end=' ')"""

"""start = int(input('start: '))
stop = int(input('stop: '))
step = int(input('step: '))
length = 0
summa = 0

for index in range(start,stop,step):
	print(index)
	length = length + 1
	summa  = summa  + index
print('Длина: ',length)
print('Сумма: ',summa)"""


length = 0
start = int(input('start: '))
stop = int(input('stop: '))

for i in range(start, stop):
	print(i,'x',i,'=',i*i)
	length = length + (i*i)
print('Длина: ',length)


"""#Факториал
start = int(input('start: '))
stop = int(input('stop: '))
san = 1

for i in range(start, stop):
	san = san * i
	print(i,'!=',san)"""
