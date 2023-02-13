'''
#1
ozgeriwshi = 'magliwmatlardin neshe turi bar?'
print(ozgeriwshi, '4-turi float, string, integer, boolean')

#2
a = ((23+17)/2)%5
print(a)

#3
print('print juwapti shigaradi, return bul funksida qollanamiz bir marte qaytaradi')

#4
a = int(input('san kiritin: '))
b = a%10
c = a//10
d = b+c
print(d)

#5
a = int(input('san kiritin: '))
b = int(input('san kiritin: '))
if a > b:
    print('a ulken b dan')
elif a < b:
    print('a kishi b dan')
else:
    print('a ten emes b ga')

#6
start = 1500
for i in range(start,2700):
    if i % 7 == 0:
        print(i,'7 ge bolinetin san')
    if i % 5 == 0:
        print(i,'5 ge bolinetin san')

#7
for i in range(7):
    if i == 3:
        continue
    elif i == 6:
        continue
    print(i)

#8
for i in range(10):
    print('men baslawshiman')

#9
for i in range(1,20):
    if i % 2 ==0:
        print('jup san', i)
    elif i % 2 == 1:
        print('taq san', i)

#10
start = 1
stop = 20
s = 0
for i in range(start, stop):
    if i > 5 and i < 15:
        s+=i
        print(i)
print(s)

#11
start = 1 
stop = 11
for i in range(start, stop):
    print(i/10*100, 'kg')

#12
start = 1
stop = 10
f = 1
for i in range(1,10):
    f *= i
    print(i)
print(f)

#13
lists = ['1', '2', '3', '4', '5']
print(lists)
lists.insert(3,'0')
print(lists)
'''
#14
import array
num = array.array('i', [])
s = 0
for i in range(5):
    print(i)
    s += i
print(s)
'''
#15
lists = ['1', '2', '3', '4', '5']
print(lists)
for list in lists:
    if lists == list.index[0]:
        print(list)

#16
list = []
print(list, 'bos spisok')
list = ['Aziz']
print(list, 'bos emes spisok')

#17
lists = tuple(['Aziz', 'Asqar', 'Atabek'])
print(lists)

#18
user = {
    'at':'Azizbek',
    'famiyliya':'Tilemisov',
    'jil':1998
}
print(user, 'gilt soz bul jerde {at}')

#19
user = {'Aziz', 'Tilemisov'}
print(user)

#20
def san():
    a = 10
    b = 20
    if a < b:
        print('a kishi b dan')
    return a,b
print(san)

#21
lists = ['1', '2', '3', '4', '5']
print(lists)

#24
import turtle
turtle.title('User')

turtle.onclick()

#25
from tkinter import *
window = Tk()
window.title('Web site')
window.resizable(False,False)
window.configure(bg='black')
window.geometry('320x240')
window.mainloop()
'''