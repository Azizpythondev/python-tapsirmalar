'''
#1
r = 1.1
p = 3.14
s = p*(r**2)
print('natiyje: ',s)

#2
name = input('atinizdi kiritin: ')
lastname = input('familiyanizdi kiritin: ')
print(name[::-1])
print(lastname[::-1])

#2
user = input('atinizdi kiritin: ')
print(user[::-1])

#3
a = int(input('a: '))
p = 4 * a
print('natiyje: ',p)

#4
a = int(input('a: '))
s = a ** 2
print('natiyje: ',s)

#5
a = int(input('a: '))
b = int(input('b: '))
s = a * b
print('natiyje: ',s)

#6
l = int(input('l: '))
a = l/100
print('metr: ',a)

#7
m = int(input('kg: '))
n = m / 1000
print('tonna: ',n)

#8
a = int(input('a: '))
if a > 0:
    print(a+1)
elif a < 0:
    print('ozgermesin')

#9
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if c < b < a:
    print(c,'kishi b dan a dan',b,a)
if a > b > c:
    print(a,'a ulken b dan c dan',b,c)

#2
a = input('Ati: ')
b = input('familiya: ')
#a = 'Aziz'
#b = 'Tilemisov'
#c = None
c = a
a = b
b = c
print('natiyje: ', a,b)
'''
#10
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a > b > c or a < b < c or b > a > c or b < a < c or c < a < b or c > a > b:
    print('ushmuyeshlik bar')
if((a == b) > c) or ((a == c) > b) or ((c == b) > a):
    print('ushmuyeshlik bar')
if a == b == c:
    print('ushmuyeshlik bar')




















