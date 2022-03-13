"""
sys_kullanıcı_adı="admin"
sys_sifre="123456"

giris_hakkı=3
while True:
    kullanıcı_adı=input("Kullanıcı Adı:")
    parola=input("Sifre:")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola ==sys_sifre):
        print("Kullanıcı adı yanlış!")
        giris_hakkı -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_sifre):
        print("Parola Hatalı")
        giris_hakkı -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_sifre):
        print("Kullanıcı adı ve şifre hatalıdır!")
        giris_hakkı -= 1
    else:
        print("Giriş Başarılı!!")
        break
    if(giris_hakkı == 0):
        print("giriş hakkınız bitmiştir.\nDaha sonra tekrar deneyiniz")
        break
"""


"""
***********************ATM MAKİNESİ************************
"""

from cgi import print_arguments


print("""****************************

\t\tATM MAKİNESİ

****************************

İşlemler:
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme

Programdan Çıkmak için 'q' tuşuna basınız!!
""")

"""bakiye=0

while True:
    işlem = input("işlemi seçiniz:")
    if(işlem=="q"):
        print("Yine bekleriz")
        break
    elif(işlem=="1"):
        print("Bakiyeniz: {}₺ ".format(bakiye))
    elif(işlem=="2"):
        miktar = int(input("Bakiye Giriniz:"))
        bakiye += miktar
    elif(işlem == "3"):
        miktar = int(input("Miktarı giriniz:"))
        if((bakiye - miktar)<0):
            print("Bakiye yetersizdir")
            continue
        bakiye -= miktar
    else:
        print("GEÇERSİZ İŞLEM SEÇTİNİZ!!!!")
"""

"""************************************************
BİR SAYININ FAKTÖRİYELİNİ BULMA 
************************************************"""


print("""************************************************
BİR SAYININ FAKTÖRİYELİNİ BULMA 
ÇIKMAK İÇİN 'q' YA BASINIZ
************************************************""")
"""
while True:
    sayı = input("Faktöriyelini bulunmasını istediğiniz sayıyı giriniz:")
    if(sayı == "q"):
        print("Program Sonlandırılıyor")
        break
    else:
        sayı = int(sayı)
        faktoriyel = 1
        for i in range(2,sayı+1):
            faktoriyel *= i
        print(faktoriyel)

"""

#************************************************************

"""
FİBONACCİ SERİSİ
"""

a=1
b=1
secım = int(input("Kaç adımlı serı olmasını ıstersınız:"))
fibonacci = [a,b]
for i in range(secım-2):
    a,b = b,a+b  #a = b, b = a+b oldu
    fibonacci.append(b)
print(fibonacci)
 