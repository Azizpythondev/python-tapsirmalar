#1
"""from array import array
from random import randint

numbers = array('i', [])
for i in range(5):
	numbers.append(randint(-50,50))

print(sorted(numbers)[::-1])"""

#reading, appending, writing

#new_file = open('users.txt', mode='a')
#new_file.write('Allayar\n')

"""read_file = open('users.txt', mode='r')
a = read_file.read()
print(a)"""

"""text = open('users.txt', mode='r', encoding='utf-8')

texts = list()
texts.append(text.read().upper())

new_texts = open('new_users.txt', mode='w', encoding='utf-8')
for i in texts:
	new_texts.write(i)"""

"""for i in texts:
	print(i)
	print(f'Длина текста {len(i)}')"""


#file = open('lyrics.txt', mode='r')


with open('lyrics.txt', mode='r') as file:
	texts = list()
	vowels = 'aeoiu'
	l_vowel = 0
	text = file.read()
	texts.append(text)
	for i in text:
		if i in vowels:
			l_vowel += 1

for i in texts:
	print(i)


print(f'Количество гласных букв {l_vowel}')
