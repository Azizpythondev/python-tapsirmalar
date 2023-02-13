#1
"""name = input('Введите имя: ').strip()
print('Здравствуй',name,'ваше имя состоит из',len(name),'букв')
print('Qalaysiz',name,'sizdin atiniz ',len(name),'haripten turadi.')

#3
first_name = input('Введите имя: ').strip().lower()
last_name = input('Введите имя: ').strip().lower()
print(first_name+last_name)"""

#5

"""user = input('word: ').lower() #Hello #hello
vowels = 'aeoiu'
if user[0] in vowels:
    user = user + 'way'
else:
    user = user[1:] + user[0] + 'ay'
print('Слово: ',user)"""


"""if user[0] == 'a':
    user = user + 'way'
if user[0] == 'e':
    user = user + 'way'
if user[0] == 'o':
    user = user + 'way'
print(user)"""


#user = input('Enter a word: ').lower()

#1-метод
"""if user[0] == 'a':
    user = user+'ay'
if user[0] == 'e':
    user = user+'ay'
if user[0] == 'b':
    user = user[1:]+user[0]+'way'
if user[0] == 'c':
    user = user[1:]+user[0]+'way'
print('Результат: ',user)

#2-метод
if user[0] == 'a' or user[0] == 'e':
    user = user+'ay'
if user[0] == 'b' or user[0] == 'c':
    user = user[1:]+user[0]+'way'
print('Результат: ',user)"""

#3-метод
"""user = input('Enter a word: ').lower()
vowels = 'aeoiu'
if user[0] in vowels:
    user = user+'ay'
else:
    user = user[1:]+user[0]+'way'
print('Результат: ',user)"""


#String -> Строка
"""word = input('Type something: ')
print(word.isalpha())
print(word.isnumeric())
print(word.islower())"""

"""
count_a = word.count('a')
count_e = word.count('e')
print(count_a, count_e, '=',count_a+count_e)"""

"""start_a = word.startswith('a')
print(start_a)

print(word.endswith('t'))

index_a = word.index('a')
print(index_a)

find_b = word.find('b')
print(find_b)"""



#Математическое функции

pi = 3.14
import math 
print(pi, math.pi)
print(round(5.98))
print(round(5.43))










