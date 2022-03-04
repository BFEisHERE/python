from calendar import c

"""
print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncunun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad,soyad,takım]
print("Bilgiler Kaydediliyor...")

print("Oyuncu Adı:\t{}\nOyuncunun Soyadı:\t{}\nOyuncunun Takımı:\t{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("Bilgiler Kaydedildi...")


print("*************************************************************************")
print("*************************************************************************")
print("*************************************************************************")
print("*************************************************************************")
print("DENKLEM KÖKLERİ BULMA")
print("Değerleri giriniz")
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

delta=float(b**2-4*a*c)

x1=float((-b-delta**0.5)/(2*a))
x2=float((-b+delta**0.5)/(2*a))
print("Birinci Kök: {}\nİkinci Kök: {}\n".format(x1,x2))
"""

#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın
"""
print("Değerleri sırasıyla giriniz")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print("Değerlerin çarpımı: {}".format(a*b*c))"""


#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""
print("Boy kilo endeksi hesaplama işlemi için\n boy ve kilonuzu giriniz!")
boy=float(input("boyunuz:"))
kilo=int(input("kilonuz:"))
print("Ekdeksiniz: {}",kilo/(boy**2))"""


#Bir aracın kilometrede ne kadar yaktığı ve
#  #kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam 
# ne kadar ödemesini gerektiğini hesaplayın.
"""
yakan = float(input("Kilometrede yakan miktar:"))
km=int(input("Kaç km yol yaptınız:"))
print("Tutar: {} ₺".format(yakan*km))"""

#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
""""
print("Sırasıyla ad soyad ve numaranızı giriniz")
ad = input("ad:")
soyad = input("soyad:")
no = input("no:")
print("\n\nadınız: {}\nsoyad: {}\nno: {}".format(ad,soyad,no))"""

#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
a = int(input("a:"))
b = int(input("b:"))
print("Sayılarınız sırasıyla: {} {}\nSayılarınızın yerleri değiştiriliyor!!!".format(a,b))
c=b
b=a
print("Yeni sayılarınız 1. sayınız:{}, 2.sayınız{}".format(c,b))"""

#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) 
# alın ve hipotenüs uzunluğunu bulmaya çalışın.

a=int(input("1. dik kenar:"))
b=int(input("2. dik kenar:"))
print("Hipotenüs Hesaplanıyor....")
c=(a ** 2 +b ** 2) ** 0.5
print("Hipotenüs= {}".format(c))