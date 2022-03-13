"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.
 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)
"""
"""boy=float(input("Boyunuzu giriniz:"))
kilo=int(input("Kilonuuz Giriniz:"))

endeks=kilo/(boy**2)
if(endeks<18.5):
    print("Zayıg")
elif(endeks>18.5 and endeks<=25):
    print("Normal")
elif(endeks>25 and endeks<=30):
    print("Fazla kilolu")
elif(endeks>30):
    print("Şişko")
else:
    print("Hatalı işlem yaptınız")"""


"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

from traceback import print_tb


a = int(input("1. sayıyı giriniz:"))
b = int(input("2. sayıyı giriniz:"))
c = int(input("3. sayıyı giriniz:"))

if (a >= b and a >= c):
    print("En büyük sayı:",a)
elif (b >= a and b >= c):
    print("En büyük sayı:",b)
elif (c >= a and c >= b):
    print("En büyük sayı:",c)
else:
    print("Hatalı işlem yaptınız")"""

"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

     Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF


vize1 = float(input("Vize1 notu:"))
vize2 = float(input("Vize2 notu:"))
final = float(input("Final notu:"))

toplam_not = (vize1*30/100)+(vize2*30/100)+(final*40/100)
if(toplam_not>=90):
    print("Harf notunuz ---> AA - {}".format(toplam_not))
elif(toplam_not>=85):
    print("Harf notunuz ---> BA - {}".format(toplam_not))
elif(toplam_not>=80):
    print("Harf notunuz ---> BB - {}".format(toplam_not))
elif(toplam_not>=75):
    print("Harf notunuz ---> CB - {}".format(toplam_not))
elif(toplam_not>=70):
    print("Harf notunuz ---> CC - {}".format(toplam_not))
elif(toplam_not>=65):
    print("Harf notunuz ---> DC - {}".format(toplam_not))
elif(toplam_not>=60):
    print("Harf notunuz ---> DD - {}".format(toplam_not))
elif(toplam_not>=50):
    print("Harf notunuz ---> FD - {}".format(toplam_not))
elif(toplam_not<50):
    print("Harf notunuz ---> FF - {}".format(toplam_not))
else:
    print("Hatalı not girdiniz!!") """

#**************************************************************

"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.
Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.
Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. 
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o
Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""
cokgen = int(input("Çokgenin kenar sayısı:"))
if(cokgen == 3):
    a = int(input("birinci kenar:"))
    b = int(input("ikinci kenar:"))
    c = int(input("üçüncü kenar:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")

elif(cokgen == 4):
    a = int(input("birinci kenar:"))
    b = int(input("ikinci kenar:"))
    c = int(input("üçüncü kenar:"))
    d = int(input("dördüncü kenar:"))
    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
else:
    print("geçersiz şekil")