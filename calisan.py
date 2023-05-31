from insan import Insan
class Calisan(Insan):
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,statu,tecrube,maas):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk)
        self.__statu=statu
        self.__tecrube=tecrube
        self.__maas=maas
        self.__zam_orani=0
        self.__yeni_maas=0
    def get_statu(self):
        return self.__statu
    def set_statu(self, new_statu):
        self.__statu = new_statu

    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,new_tecrube):
        self.__tecrube=new_tecrube

    def get_maas(self):
        return self.__maas
    def set_maas(self,new_maas):
        self.__maas=new_maas

    def get_zam_orani(self):
        return self.__zam_orani
    def set_zam_orani(self,new_zam_orani):
        self.__zam_orani=new_zam_orani


    def zam_hakki(self):
        if((self.get_tecrube() / 12)<2):
            self.__zam_orani=0
            return self.__zam_orani

        elif((self.get_tecrube() / 12)>=2 and (self.__tecrube / 12)<4 and self.__maas<15000):
            self.__zam_orani= self.__maas % self.__tecrube
            return self.__zam_orani

        elif((self.get_tecrube() / 12)>=4 and self.__maas<25000):
            self.__zam_orani= (self.__maas % self.__tecrube)/2
            return self.__zam_orani

        else:
            return self.__zam_orani

    def get_yeni_maas(self):
        self.__yeni_maas = self.get_maas() + self.zam_hakki()
        return self.__yeni_maas

    def __str__(self):
        print ("Ad:" + self.get_ad() + "  Soyad: " + self.get_soyad() + "  Tecrübe: " + str(self.get_tecrube()) + " ay   Yeni Maaş: " + str(self.get_yeni_maas()) )


