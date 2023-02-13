#Функция 

"""def sumOfTwoNumbers():
	a = 5
	b = 4
	return a + b
print(sumOfTwoNumbers())

def sumOfTwoNumbers(a,b):
	return a + b
print(sumOfTwoNumbers(10,15))"""

'''def new_len(text):
	count = 0
	for i in text:
		count += 1
	print(count)

new_len('Hello')'''
'''
def multi_ply(a,b,c):
	return a*b*c

number_1 = int(input('num_1: '))
number_2 = int(input('num_2: '))
number_3 = int(input('num_3:'))
print(multi_ply(number_1,number_2,number_3))
'''
'''
def pubg_new():
	a = int(input('a: '))
	b = int(input('b: '))
	c = int(input('c: '))
	return pow(a+b,c)

print(pubg_new())
'''
import random
import math
def power_A3(a,b):
	return pow(a,b)

def power_A234(a,b=2,c=3,d=4):
	return f"{pow(a,b)}, {pow(a,c)}, {pow(a,d)}"
def proc(x,y):
	arif = (x+y)/2 
	geomet = math.sqrt(x*y)
	return f'{arif}, {geomet}'

def triangle(a):
	p = 3*a
	s = pow(a,2) * math.sqrt(3/4)
	return f'{p}, {s}'


for i in range(5):
	m = random.randint(0,10)
	n = random.randint(0,10)
	#print(power_A3(m,n))
	#print(power_A234(m))
	#print(proc(n,m))
	#print(triangle(m))

  








