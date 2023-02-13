'''numbers = list()
for i in range(10):
    if i % 2==0:
        numbers.append(i)
print(numbers)


numbers = list(range(10))
print(numbers)
num = list(range(30))
print(num)

numbers = [i for i in range(5) if i % 2 == 0]
print(sum(numbers))
num = [i for i in range(10) if i % 2 == 1]
print(sum(num))

names = {
    'students':('Sultan','Aydos'),
    'humans': ('Alpamis','Allayar')
}
print(names)

name = {
       'homes':['Alpa', 'Aziz']
}
print(name, type(name))
'''
names = {
    'students':('Sultan','Aydos'),
    'humans': ('Alpamis','Allayar')
}
print(names)
names.update(
    {'mentor':'Atabek'}
)
print(names)
print(len(names))
print(names.keys())
print(names.values())
print(names.items())

for i , j in names.items():
    print(i,':',j)
