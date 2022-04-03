#PROBLEM1
"""
Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.
"""

# liste = ["345","sadas","324a","14","kemal"]
# for i in range(liste.__len__()):
#     try:
#         a = int(liste[i])
#         print(a)
#     except:
#         pass
#     finally:
#         print("Program Sonlandırılmıştır...")

# PROBLEM2
"""
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. 
Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
"""

# while True:
#     sayı = input("Çıkmak için q ya basınız.\nÇiftliğini sorgulamak istediğiniz sayıyı giriniz:")
#     if(sayı == "q"):
#         print("Program Sonlandırılıyor!..")
#         break
#     else:
#         try:
#             if(int(sayı) % 2 == 0):
#                 print("{} sayısı çifttir.".format(sayı))
#             else:
#                 print("{} sayısı çift değildir.".format(sayı))
#         except:
#             print("Lütfen Bir Sayı Giriniz")