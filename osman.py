"""
Harezmi
Algoritmalar(arastir)
storyboard
if()
//tek sarta gore tek sonuc
//tek sarta gore birden fazla sonuc
//birden fazla sarta gore tek sonuc
//birden fazla sarta gore birden fazla sonuc

"""
"""//tek sarta gore tek sonuc
sayigir=int(input("Lutfen sayi girniz: "))
if sayigir<50:
    print("Kaldinn")
else:
    print("Gectin")"""

#soru: \n= alt satira inmek icin kullanilir.

"""islem = int(input("Ltfn ypmk istdnz islemi secin \n 1-Toplama"))

abcd=int(input("Birinci sayi gir"))
efgh=int(input("Ikinci sayi gir"))

if islem==1:
    print(abcd+efgh)
else:
    print(abcd*efgh)"""

#soru: klavyeden takim ismi isteyecegiz. Takim ismi Fenerbahceye esit ise ne guzel takim. Aksi halde nanay

"""takim=input("Ltfn takim ismi gir: ")

if takim=="Fenerbahce":
    print("aa ne guzel takim")
else:
    print("ajfkasjfklaga")"""

#//tek sarta gore birden fazla sonuc
#soru: Ogrenci Not Puanlamasi

"""puan=int(input("Lutfen notu giriniz: "))

if puan<0:
    print("HATALI GIRIS!!")
elif puan<30:
    print("ff")
elif puan < 40:
    print("dd")
elif puan < 50:
    print("dc")
elif puan < 60:
    print("cc")
elif puan < 70:
    print("cb")
elif puan < 80:
    print("bb")
elif puan < 90:
    print("ba")
elif puan<100:
    print("aa")
else:
    print("HATALI GIRIS YAPTINIZ!!!")"""


#Soru: Klavyeden sayi alicaz.Eger bu sayi 1 olursa; klavyeden iki sayi al ve topla
#Klavyeden alinan sayi 2 ise cikarma
#Klavyeden alinan sayi 3 ise carpma
#Klavyeden alinan sayi 4 ise bolme
"""
islem=int(input("Lutfen yapacaginiz islemi secin \n 1-Toplama\n 2-Cikarma\n 3-Carpma\n 4-Bolme \n "))

if islem==1:
    birincisayi=int(input("Birinci sayiyi girin: "))
    ikincisayi = int(input("Ikinci sayiyi girin: "))
    print(birincisayi+ikincisayi)
elif islem==2:
    birincisayi = int(input("Birinci sayiyi girin: "))
    ikincisayi = int(input("Ikinci sayiyi girin: "))
    print(birincisayi - ikincisayi)
elif islem==3:
    birincisayi = int(input("Birinci sayiyi girin: "))
    ikincisayi = int(input("Ikinci sayiyi girin: "))
    print(birincisayi * ikincisayi)
elif islem==4:
    birincisayi = int(input("Birinci sayiyi girin: "))
    ikincisayi = int(input("Ikinci sayiyi girin: "))
    print(birincisayi / ikincisayi)
else:
    print("Hatali Giris yaptiniz!!")"""


#Birden Fazla Sarta Gore Tek Sonuc

"""kullaniciadi=input("Lutfen Kullanici adinizi girin: ")
sifre=input("Lutfen sifrenizi giriniz: ")

if kullaniciadi=="admin" and sifre=="1234":
    print("Giris Basarili.")
else:
    print("HATALI GIRIS!!")"""

#Soru:ise alim 30 dan buyuk ve adresi kepez olanlar ise alinsin yoksa bye bye

"""yas=int(input("Lutfen yasinizi giriniz"))
adres=input("Lutfen adresinizi giriniz")

if yas==30 and adres=="kepez":
    print("Hayirli olsun")
else:
    print("Lutfen karsida aglayiniz.")"""

#Birden Fazla Sarta Gore Birden Fazla Sonuc
"""ifelifelse"""

"""
---DONGULERRR---

1-for // sayisi belli olan donguler
2-foreach // listelerde
3-while // sonsuz ve sayisi belli olmayanlar
4-Do while // sartli donguler

"""

#for ahmet in range(1,11):
    #print(ahmet,"merhaba")

#sayi=int(input("Lutfen bir sayi giriniz: "))
#if sayi<50:
    #print("kaldi")
#else:
    #print("gecti")

#Klavyeden bir sayi aldik. BU sayi 50 den buyuk ise 5 defa gecti, aksi halde 5 defa kaldi.

"""sayi1=int(input("Lutfen bir sayi giriniz"))


if sayi1>50:
    for a in range(5):
        print("gecti")
else:
    for a in range(5):
        print("kaldi")"""

#Klavyeden 2 sayi alcaz. Yas>30 ve adres kepeze esit olursa ise alindin 5 kez. Aksi alde 5 defa bsa

"""yas=int(input("Lutfen yasinizi giriniz"))
adres=input("Lutfen adresinizi giriniz")

if yas>=30 and adres=="kepez":
    for b in range(5):
        print("ise alindiniz")
else:
    for b in range(5):
        print("bsa")"""

#klavyeden girilen 2 sayi arasindaki tek sayilari listeleyen program (%mod alma).

"""a=int(input("Birinci sayi:"))
b=int(input("Ikinci sayi:"))

for c in range(a,b):
    if c%2==1:
        print("tek sayi:",c)
"""
#ekrana 20 defa merhaba yazdir.

"""onur=0

while onur<20:
    print("merhaba")
    onur+=1"""

#klavyeden bir sayi alacaz. Bu sayi 50 den buyuk ise gecti 5 defa, aksi halde 10defa kaldi.

# sayi=int(input("Lutfen sayi giriniz:"))
#
# if sayi>50:
#      for a in range(5):
#         print("gecti")
# else:
#      ayse=0
#      while ayse<10:
#         print("kaldi")
#         ayse+=1

#Klavyeden 2sayi alicaz. Ilk sayi, ikinci sayidan kucuk oldugu surece ve 2 ile bolunenleri yazdiricaz.
# birinciSayi=int(input("ltfn birinci sayi giriniz"))
# ikinciSayi=int(input("ltfn ikinci sayi giriniz"))
#
# while birinciSayi<ikinciSayi:
#     if birinciSayi%2==0:
#         print(birinciSayi)
#     birinciSayi+=1


"""
array - dizi - liste - arraylist

"""


#klavyeden sayı al 1 olursa meyveler; farklı sayı olursa sebzeler.



# meyveler=["elma","armut","muz","çilek"]
# sebzeler=["pırasa","kabak","ıspanak","patlıcan"]
#
# sayi=int(input("bir sayi giriniz"))
#
# if sayi==1:
#     for m in meyveler:
#         print(m)
# else:
#     for s in sebzeler:
#         print(s)
#


#klavyeden bir harf al e yazılırsa erkekler k yazılırsa kadınlar listesi farkl bi harf girerse hatal giriş
#
#
#
# erkekler=["ali","veli","ahmet","mehmet"]
# kadinlar=["ayse","fatma","merve","nur"]
#
# harf=input("bir harf giriniz")
# if harf=="e":
#     for e in erkekler:
#         print(e)
# elif harf=="k":
#     for k in kadinlar:
#         print(k)
# else:
#     print("hatalı giriş")
#




# arabalar=["bmw","opel","mercedes"]
# motorlar=["honda","kavasaki"]
#
# sayi=int(input("bir sayi giriniz"))
#
# if sayi==1:
#     for a in arabalar:
#         print(a)
# else:
#     print(motorlar)
#


# antalyaIlce=["kepez","muratpasa"]
# afyonIlce=["dinar","sandıklı"]
#
# kelime=input("şehir giriniz")
#
# if kelime=="antalya":
#     for a in antalyaIlce:
#         print(a)
# elif kelime=="afyon":
#     for af in afyonIlce:
#         print(af)
# else:
#     print("hatalı giriş")

#Klavyeden girilen 2 sayi arasindaki tek sayilari giriniz.
"""sayi1=int(input("Lutfen bir sayi giriniz: "))
sayi2=int(input("Lutfen ikinci sayiyi giriniz: "))
for c in range(sayi1,sayi2):
    if c%2==1:
        print("tek sayi:",c)"""

#while ile cozum
"""while sayi1<sayi2:
    if sayi1%2==1:
        print(sayi1)
        birinci +=1 """


#Meyveler dizisi olusturup ekrana listeletin.

"""meyveler=["armut","muz","kiraz","elma","mandalina"]
print(meyveler)
"""
#RestaurantOrnegi
"""
Restauranta hosgeldin
Lutfen secimini yap
0-Exit
1-Enter
Menu Dizimiz 4 secenekli.
1-Foods
2-Soups
3-Desserts
4-Salads

"""
hesap=0
welcome=int(input("Restauranta Hosgeldiniz!\n1-Menu\n0-Exit\nPlease make your selection:"))

while True:
    if welcome == 1:
        print("Welcome,Menu is here:")
        menu = ["1-Foods", "2-Soups", "3-Desserts", "4-Salads"]
        for m in menu:
            print(m)
        selection = int(input("Please choose one of your options:"))
        if selection == 1:
            print("Foods")
            foods = ["1-Pide:30TL", "2-Manti:50TL", "3-Sarma:40TL", "4-Ciger:60TL", "5-Kofte:70TL"]
            for y in foods:
                print(y)
            foodsnumber = int(input("Please choose your food:\n"))
            if foodsnumber == 1:
                print("Seciminiz: ", foods[0])
                hesap = hesap + 30
                print("Toplam hesabiniz: ", hesap, "TL")
            elif foodsnumber == 2:
                print("Seciminiz: ", foods[1])
                hesap = hesap + 50
                print("Toplam hesabiniz: ", hesap, "TL")
            elif foodsnumber == 3:
                print("Seciminiz: ", foods[2])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif foodsnumber == 4:
                print("Seciminiz: ", foods[3])
                hesap = hesap + 60
                print("Toplam hesabiniz: ", hesap, "TL")
            elif foodsnumber == 5:
                print("Seciminiz: ", foods[4])
                hesap = hesap + 70
                print("Toplam hesabiniz: ", hesap, "TL")
            else:
                print("Incorrect Entry")
        elif selection == 2:
            print("Soups")
            soups = ["1-Merco:30TL", "2-Kello:30TL", "3-Yaylo:30TL", "4-Manto:30TL", "5-Tavo:30TL"]
            for s in soups:
                print(s)
            soupsnumber = int(input("Please choose your soup:\n"))
            if soupsnumber == 1:
                print("Seciminiz: ", soups[0])
                hesap = hesap + 30
                print("Toplam hesabiniz: ", hesap, "TL")
            elif soupsnumber == 2:
                print("Seciminiz: ", soups[1])
                hesap = hesap + 30
                print("Toplam hesabiniz: ", hesap, "TL")
            elif soupsnumber == 3:
                print("Seciminiz: ", soups[2])
                hesap = hesap + 30
                print("Toplam hesabiniz: ", hesap, "TL")
            elif soupsnumber == 4:
                print("Seciminiz: ", soups[3])
                hesap = hesap + 30
                print("Toplam hesabiniz: ", hesap, "TL")
            elif soupsnumber == 5:
                print("Seciminiz: ", soups[4])
                hesap = hesap + 30
                print("Toplam hesabiniz: ", hesap, "TL")
            else:
                print("Incorrect Entry")

        elif selection == 3:

            desserts = ["1-Baklava:40TL", "2-Kazandibi:40TL", "3-Sutlac:40TL", "4-Kabak:40TL", "5-Kunefe:40TL"]
            for d in desserts:
                print(d)
            dessertsnumber = int(input("Please choose your dessert:\n"))
            if dessertsnumber == 1:
                print("Seciminiz: ", desserts[0])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif dessertsnumber == 2:
                print("Seciminiz: ", desserts[1])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif dessertsnumber == 3:
                print("Seciminiz: ", desserts[2])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif dessertsnumber == 4:
                print("Seciminiz: ", desserts[3])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif dessertsnumber == 5:
                print("Seciminiz: ", desserts[4])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            else:
                print("Incorrect Entry")
        elif selection == 4:
            print("Salads")
            salads = ["1-Coban:40TL", "2-Gavurdagi:40TL", "3-Sezar:40TL", "4-Yesillik:40TL", "5-Avokado:40TL"]
            for sal in salads:
                print(sal)
            saladsnumber = int(input("Please choose your salads:\n"))
            if saladsnumber == 1:
                print("Seciminiz: ", salads[0])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif saladsnumber == 2:
                print("Seciminiz: ", salads[1])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif saladsnumber == 3:
                print("Seciminiz: ", salads[2])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif saladsnumber == 4:
                print("Seciminiz: ", salads[3])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            elif saladsnumber == 5:
                print("Seciminiz: ", salads[4])
                hesap = hesap + 40
                print("Toplam hesabiniz: ", hesap, "TL")
            else:
                print("Incorrect Entry")
        else:
            print("Incorrect Entry! Please Try Again.")

    elif welcome == 0:
        print("We are sad to see you go!")
    else:
        print("Incorrect Entry!")