'''
#1
keste = []
print('kestede hazir adam kiritilmegen',len(keste))

#2
keste = ['orange', 'apple']
print('kestede',len(keste), 'element bar')

#3
keste = ['orange', 'apple', 'banana']
keste.append(['kiwi', 'mandarin'])
print('kestede',len(keste), 'element bar')

#4
keste = []
print(keste)
keste.append('Azizbek')
print('kestede',len(keste),'element bar')

#5
keste = []
print(keste)
keste.insert(0,'Azizbek')
print('kestede',len(keste),'element bar')

#6
keste = []
print(keste)
keste.extend('Azizbek','Asqar', 'Aman')
print('kestede',len(keste),'element bar')

#7
keste = ['Azizbek','Begis','Timur','Sarsen', 'Uzaqbergen']
print('kestede',len(keste),'element bar', sorted(keste))
'''
#8
import random
m = int(input('m: '))
n = int(input('n: '))
print(m,'x',n,'keste')

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
			m_table[i][j] = '22'
for i in m_table:
	print(i)


