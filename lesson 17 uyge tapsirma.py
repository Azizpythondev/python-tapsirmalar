'''
#1
summa = 0
while summa <=50:
    user = int(input('user: '))
    summa += user
print('summa: ', summa)

s = 0 
is_process = True
while is_process:
    if s <= 50:
        user = int(input('user: '))
        s += user
    if s > 50:
        is_process = False
print('summa: ', summa)

summa = 0
while summa <=100:
    user = int(input('user: '))
    summa += user
print('summa: ', pow(summa,2))

summa = 0
while summa <=100:
    user = int(input('user: '))
    summa += user
    if summa % 2 == 0:
        print('jup san')
    elif summa % 2 == 1:
        print('taq san')   
print('summa: ', summa)


summa = 0
while summa <=5:
    user = int(input('user: '))
    if user >= 5:
        break
    summa += 1
print('aqirgi san: ', user)

summa = 0
party = 0
user = int(input('user: '))
while user == 'awa':
    user = int(input('user: '))
    party += 1
    summa += party
print('summa: ', summa)

party = 0
send = input('Хотите приглосить людей?').lower()
while send == 'да':
    send = input('Еще будут?').lower()
    if send == 'нет':
        break
    party += 1
print('На вечеринке уже', party, 'людей')
'''
#6
user = int(input('10 mn 20 arasindagi sandi kiritin: '))
while True:
    if user < 10:
        user_1 = int(input('qayttan basqa san kiritin '))
        print('juda tomen san kiritildi ',user)
        user += 1
    elif user > 20:
        print('juda ulken san kiritildi ', user)
        user += user_1
'''
#5
compendium = 50        
user = int(input('san kiritin: '))
while True:
    if compendium > user:
        print('juda tomen')
    elif compendium < user:
        print('juda joqari')
        user_1 = int(input('basqa san kiriitin: '))
    if compendium == user:
        print('jaqsi')
        user += 1
'''












 
