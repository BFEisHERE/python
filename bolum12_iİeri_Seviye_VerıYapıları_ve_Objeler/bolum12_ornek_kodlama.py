"""
****Sayısal veriler****
bin() -> 2 tabanındaki dönüşümü gösterir
hex() -> 16 tabanındaki dönüşümü gösterir
abs() -> mutlak değerini alır
round() -> sayıları alta veya üste yuvarlar
max() -> verilen iki değerin büyüğünü aşır 
min() -> verilen iki değerin küçüğünü alır
sum() -> onksiyonu verilen değerleri toplayarak döndürür.değerlerin liste,demet,vb. şekilde verilmesi gerekir
pow() -> fonksiyoun 2 değer alır. birincisi taban ikincisi üst değeri alır
****String Metodları****
upper() -> tüm karakterleri büyük harf yapar
loWer() -> tüm karakterleri küçük harf yapar
replace(x,y) -> stringyteki x değerlerini y ile değiştirir
startswith() ->   x ile başlıyorsa True, başlamıyorsa False döner
endswith() ->  x ile bitiyorsa True, bitmiyorsa False döner
split() -> verilen bir a değeri string parçalarla ayrılarak herbir parça listelenir
strip() -> stringin başında ve sonunda bulunan x değerlerini siler
lstrip() -> stringin sadece başında bulunan x değerini siler
rstrip() -> stringin sadece sonunda bulunan x değerini siler
join() -> listenin elemanların bir string değeriyle birleştirir
count() -> string içindeki x değerlerini sayar
find() -> x değerini stringte arar ve bulduğu indeksi döndürür bulamazsa -1 döner
rfind() -> x değerini sondan itibaren arar ve bulduğu indeksi döndürür, bulamazsa -1 döner
****Kümelerin Metodları****
add() -> kümeye eleman eklemeyi sağlar. Aynı eleman eklenmeye calısılırsa hata verir
difference() -> birinci kümenin ikinci kümeden farkını alır [küme1.difference(küme2)]
difference_update() -> farklarını bulup ekler
discard() -> kümeden elemen çıkarmayı sağlar. değer yoksa hiçbir şey yapmaz
intersection() -> iki kümenin kesişimini bulur
intersection_update() -> sonucu bulur ve ekler
isdisjoint() -> kesişim kümesi yoksa True, varsa False döndürür
issubset() -> birinci küme ikinci kümenin alt kümesi ise True, değilse False döndürür
union() -> birleşim kümesi : union() metodu
update() -> birleşim ve güncelleme : update() metodu
****Listelerin Metodları****
append() -> liste sonuna bir şey eklemeyi sağlar
extend() -> listeye başka bir listeden eleman çekmedir
insert() -> listenin belli bir indeksine veri eklemeyi sağlar
pop() -> listeden eleman çıkarılıyor
remove() -> verdiğimiz değeri listeden çıkarır
index() -> verilen karakterin hangi indexte olduğunu soyler. eğer ki değer belirlenirse. verilen değerdeki indeksten aramaya başlar
count() -> verilen değerin listede kaç tane olduğunu sayar
sort() -> #listenin elemanlarını sıralar. sayı ise küçükten büyüğü, string ise alfabetik sıralar
"""

#Örnek Uygulama
class Dosya():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8") as file:

            dosya_icerigi = file.read()
            self.sade_kelimeler = list()
            kelimeler = dosya_icerigi.split()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                
                self.sade_kelimeler.append(i)

                for i in self.sade_kelimeler:
                    print(i)
    
    def tum_kelimeler(self):

        kelimeler_kümesi = {}
        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)
        
        print("Tüm Kelimeler......")

        for i in kelimeler_kümesi:
            print(i)
            print("*****************************************")

    def kelime_frekansı(self):
        kelime_sözlük = dict()

        for i in self.sade_kelimeler:
            if(i in kelime_sözlük):
                kelime_sözlük +=  1
            
            else:
                kelime_sözlük[i] = 1
        
        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor.....").format(kelime,sayı)

            print("----------------------------------------------------")

dosya = Dosya()

dosya.tum_kelimeler()
dosya.kelime_frekansı()
