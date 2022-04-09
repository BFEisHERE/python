# Problem 1
# Elinizde uzunca bir string olsun.
#             "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
# Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""
a =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
sayı = dict()

for karakter in a:
    if (karakter in sayı):
        sayı[karakter] += 1
    else:
        sayı[karakter] = 1
for i,j in sayı.items():
    
    print(i,":",j)"""

#PROBLEM 2
#Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir 
# string oluşturun ve bu string'i ekrana yazdırın.
"""
bas_harfler = ""
with open("şiir.txt","r",encoding="utf-8") as file:
    for satır in file:
        bas_harfler += satır[0]

print(bas_harfler)"""

