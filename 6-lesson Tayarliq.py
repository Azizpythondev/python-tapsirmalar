#1
'''
a = int(input('a: '))
b = int(input('b: '))
if a > b:
    c = a
    a = b
    b = c
    print('a:',a,'b:',b)
elif a < b:
    print('a:',a,'b:',b)
'''
#3
'''     
a = int(input('a: '))
if a >= 10 and a <= 20:
    print('Спасибо')
else:
    print('Неправильный ответ!')

#5
user = input('Jawin ba? ')
if user == 'awa' or user == 'Awa':
    user = input('Samal barma? ')
    if user is 'awa' or user == 'Awa':
        print('Zontiksiz barip qayt')
    else:
        print('Zontikti alip ket')
else:
    print('Jaqsi barip qayt')
'''

#String -> Строка

text = 'Atabek'
print(text, type(text))
print(len(text))
print(text[0], text[3])

text = 'Hello'
print(text[4])

text = 's5afooewdfsd'
print(text[7])

print('s' in text)
print('S' in text)
print(text[0] in text)
print(str(5) in text)
print('s' is 's')
#length -> len

text = 'Karakalpakstan'
print(text)
print(text[0:14])
print(text[:14])
print(text[0:10:1])
print(text[:7:1])
print(text[:2])
print(text[5:8:1])
print(text[::-1])
print(text[14:10:-1])

'''
name = input('Введите имя: ')
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
'''

text = '   Atabek Murtazaev   '
print(text.strip())



























