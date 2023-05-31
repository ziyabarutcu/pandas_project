from calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,statu,tecrube,maas):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk,statu,tecrube,maas)
        self.__yipranma_payi=0.2
        self.__yeni_maas=0
        self.__zam_orani=0
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def get_zam_orani(self):
        return self.__zam_orani

    def get_yeni_maas(self):
        self.__yeni_maas = self.get_maas() * self.zam_hakki()
        return self.__yeni_maas

    def zam_hakki(self):
        if ((self.get_tecrube()/12) < 2):
            self.__zam_orani = self.__yipranma_payi*10
            return self.__zam_orani

        elif ((self.get_tecrube() / 12) >= 2 and (self.get_tecrube() / 12) < 4 and self.get_maas() < 15000):
            self.__zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10)
            return self.__zam_orani

        elif ((self.get_tecrube() / 12) >= 4 and self.get_maas() < 25000):
            self.__zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10)
            return self.__zam_orani
        else:
            return 1

    def __str__(self):
        print("Ad: "+self.get_ad() + "  Soyad: " + self.get_soyad() + "  Tecrübe: " + str(self.get_tecrube()) + " ay   Yeni Maaş: " + str(self.get_yeni_maas()))

