from insan import Insan
from issiz import Issiz
from calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

i1=Insan("123456","isim1","soyad1","35","kadın","Türk")
i1.__str__()

i2=Insan("789101","isim2","soyad2","45","erkek","Japon")
i2.__str__()



i3=Issiz("746461","isim3","soyad3","30","kadın","Türk","beyazyaka",5,"maviyaka",8,"yonetici",3)
i3.__str__()

i4=Issiz("784681","isim4","soyad4","49","erkek","Türk","beyazyaka",4,"maviyaka",3,"yonetici",4)
i4.__str__()

i5=Issiz("705401","isim5","soyad5","28","kadın","Türk","beyazyaka",6,"maviyaka",2,"yonetici",1)
i5.__str__()


def kullanici_bilgisi():
    global statu
    global tecrube
    global maas
    statu = input("Hangi Sektorde Çalışıyorsunuz? (“teknoloji, muhasebe, inşaat, diğer) :")
    while (statu != "teknoloji" and statu != "muhasebe" and statu != "inşaat" and statu != "diğer"):
        print("Lütfen doğru şekilde tekrar girin...")
        statu = input("Hangi Sektorde Çalışıyorsunuz? (“teknoloji, muhasebe, inşaat, diğer) :")
    print(statu)

    tecrube = int(input("Bu sektörde kaç ay çalıştınız? :"))
    print(tecrube)

    maas = int(input("Maaşınızı Girin :"))
    print(maas)

print("Çalışanlar....")

kullanici_bilgisi()
i6=Calisan("548613", "isim6", "soyad6", "46", "erkek", "Kanadalı", statu, tecrube, maas)
i6.__str__()

kullanici_bilgisi()
i7=Calisan("100200", "isim7", "soyad7", "66", "Kadın", "Hintli", statu, tecrube, maas)
i7.__str__()

kullanici_bilgisi()
i8=Calisan("454200", "isim8", "soyad8", "29", "Kadın", "Alman", statu, tecrube, maas)
i8.__str__()



print("Mavi Yakalılar....")

kullanici_bilgisi()
i9=MaviYaka("455550","isim9","soyad9","21","erkek","Amerikalı",statu,tecrube,maas)
i9.__str__()

kullanici_bilgisi()
i10=MaviYaka("464851","isim10","soyad10","51","erkek","Alman",statu,tecrube,maas)
i10.__str__()

kullanici_bilgisi()
i11=MaviYaka("112456","isim11","soyad11","40","kadın","Fransız",statu,tecrube,maas)
i11.__str__()


print("Beyaz Yakalılar....")

kullanici_bilgisi()
i12=BeyazYaka("684865","isim12","soyad12","50","kadın","Fransız",statu,tecrube,maas)
i12.__str__()

kullanici_bilgisi()
i13=BeyazYaka("555666","isim13","soyad13","44","kadın","Azeri",statu,tecrube,maas)
i13.__str__()

kullanici_bilgisi()
i14=BeyazYaka("321123","isim14","soyad14","32","erkek","İspanyol",statu,tecrube,maas)
i14.__str__()