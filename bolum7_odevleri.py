#PROJE1
"""
Math modülündeki hazır fonksiyonları kullanarak gelişmiş 
bir hesap makinesi geliştirmeye çalışın.
"""
from curses import savetty
import math
from select import kevent
import time

print("""Yapmak istediğiniz işlem nedir?
1:Toplama
2:Çıkarma
3:Çarpma
4:Bölme
5:Üst Alma İşlemi
6:Karekök Alma İşlemi
7:Logaritmasını Bulma İşlemi
8:Dereceyi Radyana Çevirme İşlemi
9:Radyanı Dereceye Çevirme İşlemi
10:Sinüs'ü Bılma İşlemi
11:Cosinüs'ü Bulma İşlemi
12:Tanjant'ı Bulma İşlemi
13:Cotanjant'ı Bulma İşlemi
Çıkmak için q'ya Basınız!!!!
""")

while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz:")
    
    if(işlem == "q"):
        print("işleminiz sonlandırılıyor...")
        time.sleep(2)
        print("tekrar bekleriz ... ")
        break

    elif(işlem == "1"):
        sayı1 = int(input("Birinci Sayıyı giriniz:"))
        sayı2 = int(input("Birinci Sayıyı giriniz:"))
        time.sleep(1)
        print("Toplama işlemini seçtiniz. {} + {} = {}".format(sayı1,sayı2,sayı1+sayı2))
        

    elif(işlem == "2"):
        sayı1 = int(input("Birinci Sayıyı giriniz:"))
        sayı2 = int(input("Birinci Sayıyı giriniz:"))
        time.sleep(1)
        print("Çıkarma işlemini seçtiniz: {} - {} = {}".format(sayı1,sayı2,sayı1-sayı2))
        
    
    elif(işlem == "3"):
        sayı1 = int(input("Birinci Sayıyı giriniz:"))
        sayı2 = int(input("Birinci Sayıyı giriniz:"))
        time.sleep(1)
        print("Çarpma işlemini seçtiniz: {} * {} = {}".format(sayı1,sayı2,sayı1*sayı2))
        

    elif(işlem == "4"):
        sayı1 = int(input("Birinci Sayıyı giriniz:"))
        sayı2 = int(input("Birinci Sayıyı giriniz:"))
        time.sleep(1)
        print("Bölme işlemini Seçtiniz: {} / {} = {}".format(sayı1,sayı2,sayı1/sayı2))
        

    elif(işlem == "5"):
        print("Üst Alma İşlemini Seçtiniz.")
        sayı1 = int(input("Sayının Tabanını Giriniz:"))
        sayı2 = int(input("Sayının Üstünü Giriniz:"))
        time.sleep(1)
        print("Sonuç: {}".format(math.pow(sayı1,sayı2)))
        

    elif(işlem == "6"):
        print("Karekök Alma işlemini seçtiniz.")
        sayı1 = int(input("Kök içini giriniz giriniz:"))
        time.sleep(1)
        print("Sonuç: {}".format(math.sqrt(sayı1)))
        

    elif(işlem == "7"):
        print("Logaritmasını bulma işlemini seçtiniz.")
        sayı1=int(input("Sayıyı giriniz:"))
        sayı2 = int(input("Logaritma tabanını giriniz:"))
        time.sleep(1)
        print("Sonuç: {}".format(math.log(sayı1,sayı2)))
        

    elif(işlem == "8"):
        print("Dereceyi Radyana Çevirme İşlemini Seçtiniz.")
        sayı1 = float(input("Dereceyi Giriniz:"))
        time.sleep(1)
        print("{} derecesi = {} radyandr".format(sayı1,math.degrees))
        

    elif(işlem == "9"):
        print("Radyanı dereceye çevirme işlemini seçtiniz")
        sayı1 = float(input("Radyanı Giriniz:"))
        time.sleep(1)
        print("{} radyan = {} derecedir".format(sayı1,math.radians))
        

    elif(işlem == "10"):
        print("Sinüsü bulma işlemini seçtiniz.")
        a = input("Radyan için r tuşuna, derece için d tuşuna basınız.")
        if(a == "r" or a == "R"):
            sayı1= float(input("Radyanı Giriniz:"))
            x = math.sin(sayı1)
            time.sleep(1)
            print("sin {} = {} ".format(sayı1,x))
        else:
            sayı1=float(input("Dereceyi giriniz:"))
            x = math.sin(sayı1)
            y = math.radians(x)
            print("sin {} = {}".format(sayı1,y))
    elif(işlem == "11"):
        print("Cosinüs bulma işlemi seçtiniz.")
        sayı1 = int(input(" dereceyi giriniz : "))
        time.sleep(1)
        print("cos {} = {} ".format(sayı1,math.cos(sayı1)))
    
    elif(işlem == "12"):
        print("Tanjantı Bulma İşlemini Seçtiniz.")
        sayı1 = float(input("Dereceyi Giriniz:"))
        time.sleep(1)
        print("tan {} = {}".format(sayı1,math.tan(sayı1)))

    elif(işlem == "13"):
        print("Cotanjantı Bulma İşlemini Seçtiniz.")
        sayı1 = float(input("Dereceyi Giriniz:"))
        time.sleep(1)
        print("cot {} = {}".format(sayı1,math.cos(sayı1)/math.sin(sayı1)))

        




#PROJE2
"""
Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) 
yazmaya çalışın ve bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.
"""