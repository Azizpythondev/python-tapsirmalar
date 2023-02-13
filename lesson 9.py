'''
#1
name = input('what is your name? ')
print(name *3)

#1
name = input('what is your name? ')
start = int(input('start: '))
stop = int(input('stop: '))
for i in range(start,stop):
    print(name)

#2
name = input('what is your name? ')
start = int(input('start: '))
stop = int(input('stop: '))
for i in range(start,stop):
    print(name)
'''
'''
#3
name = input('what is your name? ')
for i in name:
    print(i, end=' ')

#4
name = input('what is your name? ')
for i in name:
    print(i, end=' ')
'''
text = 'Azizbek'
for i, x in enumerate(text):
    print(i, x, end=' ')
'''
#5
length = 0
start = int(input('start: '))
stop = int(input('stop: '))

for i in range(start, stop):
	print(i,'x',i,'=',i*i)
	length = length + (i*i)
print('Длина: ',length)
#6
lenght = 0
start = int(input('start: '))
stop = int(input('stop: '))
for i in range(start,stop):
    print(i)

#6
num = int(input('50 den tomen san kiritin: '))
for i in range(num):
    if num < 50:
        print(i)
else:
    print("Sikl tawsildi")
'''
