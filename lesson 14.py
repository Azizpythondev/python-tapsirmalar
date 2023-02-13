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
'''
#4
start = 'awa'
while start == 'awa':
    print('jenil keyin')
    continue
    if start == 'yaq':
        print('qalin keyin')
        start+=1
    break

again = 'yes'
while again == 'yes':
    print('hello')
    again=input('do you want to loop again')     

