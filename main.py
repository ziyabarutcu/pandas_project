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