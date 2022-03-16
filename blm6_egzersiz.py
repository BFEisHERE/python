#ASAL SAYILARI BULMA PROGRAMI

def asal_mı(sayı):
    if(sayı == 1):
        return False
    elif(sayı == 2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return False
        return True

while True:
    sayı = input("Sayı:")

    if(sayı == "q"):
        print("Program durduruluyor...")
        break
    else:
        sayı =int(sayı)

        if(asal_mı(sayı)):
            print(sayı," asal bir sayıdır")
        else:
            print(sayı," asal bir sayı değildir")



#Bir SAYININ TAM BÖLENİNİ BULAN PROGRAM

def tambolenlerı(sayı):
    tam_bolenler=[]
    for i in range(1,sayı):
        if(sayı%i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:

    sayı = input("Sayı:")
    if(sayı == "q"):
        print("Program durduruluyor....")
        break
    else:
        sayı=int(sayı)
        print("Sayının tam bölenleri: ",tambolenlerı(sayı))