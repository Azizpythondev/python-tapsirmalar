'''
#1
for i in range(1,21):
    print(i)

#2
n = int(input('n: '))
for i in range(n):
    if i % 3 == 0 and i % 6 == 0:
        print(i)

#3
n = int(input('n: '))
for i in range(1,n):
    if i % 5 == 0 or i % 10 == 5:
        continue
    print(i)

#4
n = int(input('n: '))
s = 0
for i in range(1,n):
    if i % 5 == 0 or i % 10 == 5:
        continue
    print(i)
    s += i
print('summa', s)

#6
n = int(input('n: '))
i = 0
while i < n:
    print(i)
    i += 1

#7
text = input('text: ')
while True:
    print(len(text))
    i += 1

#8
n = int(input('n: '))
i = 1
f = 1
while i < n:
    print(i)
    f *= i
    i += 1
print('kobeyme', f)

#9
n = int(input('n: '))
i = 0
s = 0
while i < n:
    print(i)
    i += 1
    s += i
print('summa', s)
'''
#10

n = int(input('n: '))
f = 1
s = 0
i = 1
while i <= n:
    print(i)
    f *= i
    s += f
    i += 1
print('kobeymesi',f)
print('qosindisi',s)

