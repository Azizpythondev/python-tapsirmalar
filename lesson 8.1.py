'''
#1
a = float(input('a: '))
b = a * 2
print('natiyje: ',b)

#2
a = float(input('a: '))
print('natiyje: ',round(a,2))

#3
b = int(input('b: '))
c = b ** (1/2)
print('natiyje: ', round(c,2))

#4
a = 3.141592653589793238462643
print('natiyje: ',round(a,5))

#5
r = float(input('radius: '))
pi = 3.14
s = r * pi
print('natiyje: ',s)

#6
r = float(input('radius: '))
t = float(input('terenlik: '))

#7
a = int(input('a: '))
b = int(input('b: '))
c = (a / b) % b
print('natiyje: ' , c)

#9
text = input('text kiritin: ').lower()
if text[0] == 'b':
    print(text)
elif text[::1] == 'v':
    print(text)
else:
    print('qate juwap shiqsin')
'''
#10
text = input('text kiritin: ')
if text == 'aeuio':
    text = text + text[0]
else:
    text = text[1:] + text[0]
print('Слово: ',text)












