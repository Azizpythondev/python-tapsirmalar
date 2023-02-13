#9
# 5**2=25 pow(5,2)=25 5*5=25
"""a = int(input('a: '))
b = int(input('b: '))
summa = 0
for i in range(a,b+1):
	print(pow(i,2), end=' ')	
	summa += pow(i,2)
print('\nСумма:',summa)"""

#11
"""N = int(input('N: '))
summa = 0
for i in range(1,N+1):
	summa += pow((2*i),2)
print('Сумма:',summa)
"""
#10
"""
N = int(input('N: '))
summa = 0
for i in range(1,N+1):
	summa = summa + (1/i)
	print('Сумма:',summa)

"""
"""#12
N = int(input('N: '))
fact = 1
for i in range(11,N+1):
	print(i/10)
	fact *= i/10
print(fact)
"""
"""a = int(input('a: '))
summa_o = 0
summa_e = 0
#range(1,a+1,2)
for i in range(1,a+1):
	if i % 2 == 0:
		summa_o += i
	if i % 2 == 1:
		summa_e += i
print('Сумма четных чисел',summa_o)
print('Сумма нечетных чисел', summa_e)
"""


#Фибоначчи 
"""a = 0
b = 1
summa = 0
N = int(input('N: '))
for i in range(N):
	a,b = b,a+b
	print(i,':',b)
"""
"""
for i in range(1):
	for j in range(3):
		print(i, end=' ')
	print()
"""
"""for i in range(1,6):
	for j in range(i):
		for k in range(j):
			print('*', end=' ')
	print()"""

for i in range(1,10):
	for j in range(i):
		print('*', end=' ')
	print()

for i in range(10,0,-1):
	for j in range(i):
		print('*', end=' ')
	print()





























