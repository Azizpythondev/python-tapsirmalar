'''
import random
massiv = list()
n = int(input('n: '))
for i in range(n):
    massiv.append(n)
    print(massiv)

import random
num = list()
for i in range(10):
    num.append(random.randrange(0,10))
print(num)

#1
num = list()
for i in range(10):
    if i%2 == 1:
        num.append(i)
print(num)

#2
n = int(input('n: '))
num = list()
f = 1
i = 1
for i in range(n):
    i += 1 
    f = i*i
    num.append(f)
print(num)
'''
import turtle
turtle.bgcolor('red')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()
