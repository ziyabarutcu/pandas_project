from insan import Insan
class Issiz(Insan):
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,beyazyaka,yil1,maviyaka,yil2,yonetici,yil3):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk)
        self.__statu=""
        self.__beyazyaka=beyazyaka
        self.__yil1=yil1
        self.__maviyaka = maviyaka
        self.__yil2 = yil2
        self.__yonetici = yonetici
        self.__yil3 = yil3

    def get_statu(self):
        return self.__statu
    def set_statu(self,new_statu):
        self.__statu=new_statu


    def get_beyazyaka(self):
        return self.__beyazyaka
    def set_beyazyaka(self,new_beyazyaka):
        self.__beyazyaka=new_beyazyaka

    def get_yil1(self):
        return self.__yil1
    def set_yil1(self,new_yil1):
        self.__yil=new_yil1



    def get_maviyaka(self):
        return self.__maviyaka
    def set_maviyaka(self,new_maviyaka):
        self.__maviyaka=new_maviyaka

    def get_yil2(self):
        return self.__yil2
    def set_yil2(self,new_yil2):
        self.__yil=new_yil2


    def get_yonetici(self):
        return self.__yonetici
    def set_yonetici(self,new_yonetici):
        self.__yonetici=new_yonetici

    def get_yil3(self):
        return self.__yil3
    def set_yil3(self,new_yil3):
        self.__yil=new_yil3


    def get_statu_bul(self):
        __sozluk={self.__beyazyaka : self.__yil1, self.__maviyaka : self.__yil2 , self.__yonetici : self.__yil3 }
        a=0.35 * __sozluk[self.__beyazyaka]
        b=0.20 * __sozluk[self.__maviyaka]
        c=0.45 * __sozluk[self.__yonetici]

        if (a > b):
            if (a > c):
                self.__statu=self.__beyazyaka
                return self.__statu
            elif (c > a):
                self.__statu = self.__yonetici
                return self.__statu
        elif (b > a):
            if (b > c):
                self.__statu = self.__maviyaka
                return self.__statu
            elif (c > b):
                self.__statu = self.__yonetici
                return self.__statu
        """
        x=[a,b,c]
        max=0
        for i in x:
            if(max<i):
                max=i
        print(max)
        """
    def __str__(self):
        print(self.get_ad() + " " + self.get_soyad() + " " + self.get_statu_bul())

"""
c=Issiz("123","ziya","barutcu","21","erkek","Türk","beyazyaka",4,"maviyaka",4,"yonetici",4)
c.__str__()
"""
