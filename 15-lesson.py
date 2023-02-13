#1
'''
i = 0
while i < 5:
	print('I love python!')
	i += 1
'''
#2
"""i = 0
while i < 5:
	if i == 3:
		break
	print('I love python!')
	i += 1"""
#4
"""i = 0
while i < 10:
	if i == 3:
		print('i is',i)
		i += 1
	elif i == 6:
		print('i is',i)
		i += 1
	else:
		print('i is',i)
		i += 1"""

"""#6
text = input('text: ')
i = 0
while i < len(text):
	if text[i] == text[0] or text[i] == text[2]:
		i += 1
		continue
	print(i,':',text[i])
	i+=1

#7
n = 1
while n == 1:
	number = int(input('n: '))"""
	

#8
n = int(input('Enter your number: '))
a = 0
f = 1
#n = num

while n > 0:
	result = n % 2
	a += result*f
	f *= 10 
	n = n // 2
print(n,'целое число и',a,'бинарное число')

