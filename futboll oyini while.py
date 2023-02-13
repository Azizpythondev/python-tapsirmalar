import random

userScore = 0
compScore = 0
komp_udar = 0

while komp_udar != 5:
    a = input("qaysi jaqqa tewesiz: \n shepke, ortag'a, ong'a \n")
    b = ["shep", "orta", "on'"]
    c = random.choice(b)

    print('udar')
    print("Kompyuter " + c + "ge atildi")
    if a == c:
        print('seyvv')
        print("User: " + str(userScore) + "\n Komp: " + str(compScore))
    elif a!="shep" and a!="orta" and a!="on":
        print("oyinshi qate tepdi")
    else:
        print("gool")
        userScore += 1
        print("User: " + str(userScore) + "\n Komp: " + str(compScore))
    ot = input("Qaysi tarepke atilasiz: ")
    b = ["shep", "orta", "on'"]
    cd = random.choice(b)
    komp_udar += 1
    print("Kompyuter " + cd + "ge tepdi")
    if ot == cd:
        print("Seyvvv")
        print("User: " + str(userScore) + "\n Komp: " + str(compScore))
    else:
        print("gool")
        compScore +=1
        print("User: " + str(userScore) + "\n Komp: " + str(compScore))
    if komp_udar == 5:
        print("oyin tawsildi")
        if userScore > compScore:
            print("siz uttiniz")
        elif compScore > userScore:
            print("kompuyuter utti, siz utildiniz")
        else:
            print("tenge ten")
