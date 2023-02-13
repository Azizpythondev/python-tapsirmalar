'''
#1
a = int(input('a: '))
if a > 0:
    print(a+1)
elif a < 0:
    print(a)

#2
a = int(input('a: '))
if a > 0:
    print(a+1)
elif a < 0:
    print(a-2)

#3
a = int(input('a: '))
if a > 0:
    print(a+1)
if a < 0:
    print(a-2)
if a == 0:
    print(10)
    
#4
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d=0
e=0
if a>0:
    d=d+1
    e=e+1
if b>0:
    d=d+1
    e=e+1
if c>0:
    d=d+1
    e=e+1
print('on sanlar sani',d)

#5
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d=0
e=0
if a>0 or a<0:
    d=d+1
else:
    e=e+1
if b>0 or b<0:
    d=d+1
else: 
    e=e+1
if c>0 or c<0:
    d=d+1
else:
    e=e+1

print('on sanlar sani',d)
print('teris sanlar sani',e)

#1
import array
numbers = array.array('i', [])
for i in range(5):
    num = int(input('num: '))
    numbers.append(num)
print(numbers)
print(f'sortirovka {sorted(numbers)}')
print(len(numbers))

#2
import array
numbers = array.array('i', [])
for i in range(5):
    num = int(input('num: '))
    numbers.append(num)
print(numbers)
'''
#3
import array
numbers = array.array('i', [])
for i in range(5):
    num = int(input('num: '))
    if 10 < num and 20 > num:
        numbers.append(num)
    else:
        print('tashqarida')
    print(numbers)
