"""
a = 5;
print("sayı = ",a,end="");
print("burak")
print("burak","furkan","erkemen",sep="-");
print("birinci sayı {},ikinci sayı {}".format(31,13))
"""
"""
num1 = int(input("Birinci sayıyı giriniz= "))
num2 = int(input("İkinci sayıyı giriniz= "))
print("Girilen sayıların toplamları= ",num1+num2)
"""

"""
a = 2
a = a**2
dir(a)
print(a.bit_length())

print(a.__abs__()) #sayının mutlak değeri
print(type(a))"""

"""
a = int(input("Sayı giriniz = "))
if  a > 0:
    print(a**2);
elif a < 0:
    print(a**a);
else:
    print("sayı sıfırdır");
"""

"""
a = [1,2,3,4,5,6,7,8,9,"sayılar"]
print(len(a))
print(a.reverse())
print(a.pop(0))
for i in range(0,len(a)):
    print(a[i])
print(a.append(":)"))
print(a.insert(0,1))
for i in range(0,len(a)):
    print(a[i])
"""



from calendar import c
from functools import reduce
from tkinter import W, Y

"""
def hesapla(a,b):
    c = 0
    for x in range(a):
        c += b
    return print(c)

print(hesapla(7,5))
"""
#Bu program verilen n sayısına göre f=1+2+4+...+2^n serisini hesaplar
"""
f = 0
n = 3
for i in range(n):
    f+=2**i
    print(f)

print("sonuc= ",f)
"""
#Bu program verilen n sayısına göre
#f=1/1+1/2+1/4+...+1/(2^n) serisini hesaplar
#f toplamında 1./(2**i) işlemde yuvarlatma yapılmaması
#double olarak işlem yapması içindir
"""
f = 0
n = 10
for i in range(n):
    f +=1/(2**i)

print("sonuc=",f)
"""

# ilk 100 fibonacci yazdırma
"""
a = 1
b = 1
c = 1

for x in range(100):
    a,b = b,c
    print(c)
    c = a+b
"""

# BİRİM MATRİSİ OLUŞTURMA

"""
n = 5
x = list()
for i in range(n):
    y = list()
    for j in range(n):
        y.append(1) if i ==j else y.append(0)
    x.append(y)
"""

"""
a = range(11)
def suz(x,y):
    return x+y

print(reduce(suz,a))


def carp(x,u):
    return x*u
print(carp(1,2))
x = 1
u=2
carpma = lambda x,u:x*u
print(carpma)"""



#metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
#tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
#isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
#yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
#adı piton yılanından gelmez."""

#harf = input("sorgulanmak istenen harf:")

#sayı = []

#for s in metin:
#   if harf == s:
#        sayı +=harf

#print(len(sayı))
"""
for x in range(2,100):
    kontrol = True
    for i in range(2,x):
        if x%i == 0:
            kontrol = False
            break
        if kontrol:
            print(x)"""

"""
def asalmi(x = 2):
    asal = True
    for i in range(2,(x/2)):
        if x%i ==0:
            asal = False
            break
        else:
            return asal

x = 107
if asalmi(x):
    print(x," asal sayidir")
else:
    print(x," asal değildir")"""


"""
import random

liste = list()
for i in range(random.randint(1,1000)):
    liste.append(random.random())

x,s=len(liste),sum(liste)

print(x,"tane elemandan oluşan listenin toplamı= ",s,"ortalaması= ",s/x)"""



