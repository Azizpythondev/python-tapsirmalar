'''
#1
start = 1
stop = 5
while start <= stop:
    print('I love you',start)
    start+=1
  
#2
start = 1
stop = 5
while start <= stop:
    if start == 3:
            continue
    print('I love you python', start)
    start+=1

#3
start = 1
stop = 5
while start <= stop:
    if start > 3 and start <= 5:
        print('I love you python',start)
    start+=1

#5
start = 10
stop = 100
while start <= stop:
    print(start)
    start+=10

#4
start = 'awa'
while start == 'awa':
    print('jenil keyin')
    start = input('kun issi terlep ketesen')
    if start == 'yaq':
        print('qalin keyin')
        start = input('tonip qalasan')
        start+=1

#6
start = input('tekst kiritin: ')
stop = input('tekst kiritin: ')
while start <= stop:
    if stop >= start and start <= stop:
        print(start(len[2]))
    start+=1

#7
i = 0
while True:
    print(i)
    i+=1

#9
i = 0
s = 0
while i <= 10:
    print(i)
    i+=1
    s+=i
print(s/i)
'''
#10
start = int(input('start: '))
stop = int(input('n: '))
while start <= stop:
    print(pow(start,2))
    start += 1
print(start[len(start)])
'''
#13
start = 1
stop = 30
summa = 0
while start < stop:
    if start % 2 == 0:
        print(start)
        summa+=start
    start+=1
print('summa ', summa)

#14
start = 1
stop = 30
summa = 0
while start < stop:
    if start % 2 == 1:
        print(start)
        summa+=start
    start+=1
print('summa ', summa)

#15
start = 1
stop = int(input('n: '))
fact = 1
while start < stop:
        print(start)
        start+=1
        fact*=start
print(fact)

#11
start = 4
stop = int(input('n: '))
while start <= stop:
    print(start)
    start+=4
'''
text = 'Azizbek'
print(len(text))

 
