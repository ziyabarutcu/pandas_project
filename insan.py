class Insan:
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk):
        self.__tc_no=tc_no
        self.__ad=ad
        self.__soyad=soyad
        self.__yas=yas
        self.__cinsiyet=cinsiyet
        self.__uyruk=uyruk

    def get_tc_no(self):
        return self.__tc_no
    def set_tc_no(self,new_tc_no):
        self.__tc_no=new_tc_no

    def get_ad(self):
        return self.__ad
    def set_ad(self,new_ad):
        self.__ad=new_ad

    def get_soyad(self):
        return self.__soyad
    def set_soyad(self,new_soyad):
        self.__soyad = new_soyad

    def get_yas(self):
        return self.__yas
    def set_yas(self,new_yas):
        self.__yas = new_yas

    def get_cinsiyet(self):
        return self.__cinsiyet
    def set_cinsiyet(self,new_cinsiyet):
        self.__cinsiyet = new_cinsiyet

    def get_uyruk(self):
        return self.__uyruk
    def set_uyruk(self,new_uyruk):
        self.__uyruk = new_uyruk

    def __str__(self):
        print(self.__tc_no+" "+self.__ad+" "+self.__soyad+" "+self.__yas+" "+self.__cinsiyet+" "+self.__uyruk)

e1=Insan("123456","ziya","barutcu","21","erkek","Türk")
e1.__str__()
