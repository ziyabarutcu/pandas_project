from calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,statu,tecrube,maas):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk,statu,tecrube,maas)
        self.__tesfik_primi=500
        self.__zam_onerisi=0
        self.__yeni_maas=0


    def get_tesfik_primi(self):
        return self.__tesfik_primi
    def set_tesfik_primi(self,new_tesfik_primi):
        self.__tesfik_primi = new_tesfik_primi

    def get_zam_onerisi(self):
        return self.__zam_onerisi
    def se__zam_onerisi(self,ne__zam_onerisi):
        self.__zam_onerisi = ne__zam_onerisi

    def get_yeni_maas(self):
        self.__yeni_maas = self.get_maas() + self.zam_hakki()
        return self.__yeni_maas

    def zam_hakki(self):
        if((self.get_tecrube()/12) < 2):
            self.__zam_onerisi = self.__tesfik_primi
            return self.__zam_onerisi

        elif((self.get_tecrube()/12) >= 2 and (self.get_tecrube()/12) < 4 and self.get_maas() < 15000):
            self.__zam_onerisi = ( ( self.get_maas() % self.get_tecrube() ) * 5 ) + self.__tesfik_primi
            return self.__zam_onerisi

        elif((self.get_tecrube()/12) >= 4 and self.get_maas() < 25000):
            self.__zam_onerisi = ( ( self.get_maas() % self.get_tecrube() ) * 4 ) + self.__tesfik_primi
            return self.__zam_onerisi
        else:
            self.__zam_onerisi=self.get_maas()*0.14
            return self.__zam_onerisi
    def __str__(self):
        print("Ad: "+self.get_ad() + "  Soyad: " + self.get_soyad() + "  Tecrübe: " + str(self.get_tecrube()) + " ay   Yeni Maaş: " + str(self.get_yeni_maas()))
