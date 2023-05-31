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



veri={
    "Statü":["çalışan","çalışan","çalışan","mavi yakalı","mavi yakalı","mavi yakalı","beyaz yakalı","beyaz yakalı","beyaz yakalı"],
    "TC No":[i6.get_tc_no(),i7.get_tc_no(),i8.get_tc_no(),i9.get_tc_no(),i10.get_tc_no(),i11.get_tc_no(),i12.get_tc_no(),i13.get_tc_no(),i14.get_tc_no()],
    "Ad":[i6.get_ad(),i7.get_ad(),i8.get_ad(),i9.get_ad(),i10.get_ad(),i11.get_ad(),i12.get_ad(),i13.get_ad(),i14.get_ad()],
    "Soyad":[i6.get_soyad(),i7.get_soyad(),i8.get_soyad(),i9.get_soyad(),i10.get_soyad(),i11.get_soyad(),i12.get_soyad(),i13.get_soyad(),i14.get_soyad()],
    "Yaş":[i6.get_yas(),i7.get_yas(),i8.get_yas(),i9.get_yas(),i10.get_yas(),i11.get_yas(),i12.get_yas(),i13.get_yas(),i14.get_yas()],
    "Cinsiyet":[i6.get_cinsiyet(),i7.get_cinsiyet(),i8.get_cinsiyet(),i9.get_cinsiyet(),i10.get_cinsiyet(),i11.get_cinsiyet(),i12.get_cinsiyet(),i13.get_cinsiyet(),i14.get_cinsiyet()],
    "Uyruk":[i6.get_uyruk(),i7.get_uyruk(),i8.get_uyruk(),i9.get_uyruk(),i10.get_uyruk(),i11.get_uyruk(),i12.get_uyruk(),i13.get_uyruk(),i14.get_uyruk()],
    "Sektör":[i6.get_statu(),i7.get_statu(),i8.get_statu(),i9.get_statu(),i10.get_statu(),i11.get_statu(),i12.get_statu(),i13.get_statu(),i14.get_statu()],
    "Tecrübe":[i6.get_tecrube()/12,i7.get_tecrube()/12,i8.get_tecrube()/12,i9.get_tecrube()/12,i10.get_tecrube()/12,i11.get_tecrube()/12,i12.get_tecrube()/12,i13.get_tecrube()/12,i14.get_tecrube()/12],
    "Maaş":[i6.get_maas(),i7.get_maas(),i8.get_maas(),i9.get_maas(),i10.get_maas(),i11.get_maas(),i12.get_maas(),i13.get_maas(),i14.get_maas()],
    "Yıpranma Payı":["0","0","0",i9.get_yipranma_payi(),i10.get_yipranma_payi(),i11.get_yipranma_payi(),"0","0","0"],
    "Teşfik Primi":["0","0","0","0","0","0",i12.get_tesfik_primi(),i13.get_tesfik_primi(),i14.get_tesfik_primi()],
    "Yeni Maaş":[i6.get_yeni_maas(),i7.get_yeni_maas(),i8.get_yeni_maas(),i9.get_yeni_maas(),i10.get_yeni_maas(),i11.get_yeni_maas(),i12.get_yeni_maas(),i13.get_yeni_maas(),i14.get_yeni_maas()]
}
df=pd.DataFrame(veri)
df.to_excel("output.xlsx")

a=pd.read_excel('output.xlsx')
a=a.set_index('Number')  # a= bu dataframin baştaki indisini Number olarak güncelledik
print("Dataframe:")
print(a)
print("\n")

b=a['Maaş']>15000  # b= maaşı 15binden büyük olanlar
print("Maaşı 15binden fazla olan kişi sayısı :")
print(len(a[b]))
print("\n")


calisanlar= a['Statü']=="çalışan" #  çalışanlar
calisanlar_df=(a[calisanlar]) # calisanlar_df # = çalışanların listelendiği dataframe

toplam_maas_calisanlar= calisanlar_df['Maaş'].sum()  # çalışanların maaşlarının toplamı
ortalama_maas_calisanlar= toplam_maas_calisanlar / len(calisanlar_df)


mavi_yakalilar=a['Statü']=="mavi yakalı" # mavi yakalılar
mavi_yakalilar_df=(a[mavi_yakalilar]) # mavi_yakalılar_df= mavi yakalıların listelendiği dataframe

toplam_maas_maviyakalilar= mavi_yakalilar_df["Maaş"].sum() # mavi yakalıların maaşları toplamı
ortalama_maas_maviykalilar= toplam_maas_maviyakalilar / len(mavi_yakalilar_df)


beyaz_yakalilar=a['Statü']=="beyaz yakalı" # beyaz yakalılar
beyaz_yakalilar_df=(a[beyaz_yakalilar]) # beyaz_yakalılar_df= beyaz yakalıların listelendiği dataframe

toplam_maas_beyazyakalilar= beyaz_yakalilar_df["Maaş"].sum() # beyaz yakalıların maaşları toplamı
ortalama_maas_beyazyakalilar= toplam_maas_beyazyakalilar / len(beyaz_yakalilar_df)


print("Çalışanların ortalama maaşı:")
print(ortalama_maas_calisanlar)

print("Mavi Yakalıların ortalama maaşı:")
print(ortalama_maas_maviykalilar)


print("Beyaz Yakalıların ortalama maaşı:")
print(ortalama_maas_beyazyakalilar)
print("\n")

print("Yeni Maaşa göre dataframe sıralaması")
print(a.sort_values('Yeni Maaş'))
print("\n")

x=beyaz_yakalilar_df['Tecrübe']>3 # beyaz yakalılar dataframeindeki tecrübe değeri 3 ten büyük olanlar = x
print("3 Yıldan fazla tecrübesi olan beyaz yakalılar:")
print(beyaz_yakalilar_df[x]) # beyaz yakalılar dataframindeki xleri yazdırır
print("\n")


print("Yeni maaşı 10000 TL üzerinde olanlar (2-5 satır için):")
y=a['Yeni Maaş']>10000
xx=a[y]
xxx=(xx[["TC No" , "Yeni Maaş"]])
print(xxx.iloc[2:5])
print("\n")

assym=a[["Ad","Soyad","Sektör","Yeni Maaş"]]
new_df=pd.DataFrame(assym)
print("yeni dataframe:")
print(new_df)