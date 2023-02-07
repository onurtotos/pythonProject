
""" Aciklama Kismini yazabilirsiniz. veya # isareti ile"""

"""
Yazilimci olabilmek icin;

1-Degiskenler
2-Kosullar ve Donguler
3-Methodlar
4-Siniflar
5-Nesneler

"""

"""
1-)Degisken:

// a) Sayilar
     
     TamSayi (int) ve Ondalikli Sayi(float-double)
    
   b) Yazilar
   c) Durumlar

"""
"""print("onur totos")
birincisayi=50
ikincisayi=60
toplam=birincisayi+ikincisayi
print(toplam)

ayse=50
fatma="kelime"
hayriye=0.5
zeynep="A"

print(fatma,(birincisayi+ikincisayi))

print("Carpma islem sonucu: ", birincisayi*ikincisayi)
print("Cikarma islemi sonucu: ", birincisayi-ikincisayi)
print("Bolme islemi sonucu: ", birincisayi/ikincisayi)

""""""onur= int(input("Lutfen bir sayi gir: "))
fener=int(input("Lutfen bir sayi gir: "))
print("Toplama islemi sonucu: ", onur+fener) """
"""

#Soru1: Bir evde 3 kardes varmis. Bu 3 kardesin yaslari klavyeden girilecek ve ortalamasi hesaplansin.

a=int(input("Birinci kardesin yasini giriniz: "))
b= int(input("Ikinci kardesin yasini giriniz: "))
c=int(input("Ucuncu kardesin yasini giriniz: "))
d=(a+b+c)/3
print("Kardeslerin yaslarinin ortalamasi: ", d)


#Soru2: Bir evde 3 kardes varmis. Bu kardeslerin boylari klavyeden alincakmis. Boylar ondalikli girilecek. Ortalama?
a=float(input("Birinci kardesin boyunu giriniz: "))
b= float(input("Ikinci kardesin boyunu giriniz: "))
c=float(input("Ucuncu kardesin boyunu giriniz: "))
e=(a+b+c)/3
print("Kardeslerin boylarinin ortalamasi: ", e, "metre")


#Soru3: Ayse'nin bana 750 TL borcu var.
isim= input("Lutfen Isim Giriniz: ")
para=int(input("Lutfen miktar giriniz: "))
print(isim,"'nin bana",para, "TL borcu var.")



#Soru4: Ahmet'in bana 12.Ayda verecegi 500 TL yerine 7.Ayda 200 TL verdi.(degiskenler isim,ay sayilari, para sayilari)
isim= input("Lutfen isim giriniz: ")
birinciay= int(input("Lutfen birinci ayi giriniz: "))
tutar1=int(input("ilk Tutari giriniz: "))
ikinciay= int(input("Lutfen ikinci ayi giriniz: "))
tutar2=int(input("ikinci tutari giriniz:"))

print("{0}'in bana {1}.Ayda verecegi {2} TL yerine {3}.Ayda {4} TL verdi.".format(isim,birinciay,tutar1,ikinciay,tutar2))"""


sayi1=int(input("Lutfen sayi giriniz: "))
sayi2=int(input("Lutfen sayi giriniz: "))
sayi3=int(input("Lutfen sayi giriniz: "))

l=sayi1+sayi2+sayi3
print("sayilarin toplami: ", l)

