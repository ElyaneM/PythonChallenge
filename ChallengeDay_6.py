"""
 ChallengeDay_6

"""

# Ders 63------------------------------------

# import imp
# from tkinter import Y


# class Car():
#     modeli = "Mercedes"
#     rengi = "Qirmizi"
#     sureti = "220"

# car1 = Car()

# car2 = Car()

# print(car1.modeli)  # Mercedes
# print(car2.modeli)  # Mercedes

# #-------------------------------

# class Araba():

#     def __init__(self,model = "Melumat yoxdu",reng = "Melumat yoxdu",suret = "Melumat yoxdu"):
#         self.model = model
#         self.reng = reng
#         self.suret = suret

# car1 = Araba("BMW","Qara")
# car2 = Araba("Niva","Pink",180)
# print(car1.suret)
# print(car2.model)

# # Ders 63 bitdi------------------------------


# # Ders 64------------------------------------

# # class Programmer():

# #     def __init__(self,ad, soyad, maas,diller):
# #         self.ad = ad
# #         self.soyad = soyad
# #         self.maas = maas
# #         self.diller = diller

# #     def melumatlar(self):
# #         print("""
# #         Ad = {}
# #         Soyad = {}
# #         Maas = {}
# #         Diller = {}
# #         """.format(self.ad,self.soyad,self.maas,self.diller))   

# #     def maas_artir(self,miqdar):
# #         print("Maas artirilir...")

# #         self.maas += miqdar

# #     def dil_artir(self,dil):
# #        print("Dil artirilir...")

# #        self.diller += dil


# # programci = Programmer("Elyane","Mehiyeva",5000,["HTML","Css","Javascript","Python"])      

# # print(programci)
# # print(programci.maas_artir)
# # print(programci.dil_artir)

# # programci.melumatlar()
# # programci.maas_artir(1000)
# # programci.melumatlar()
# # programci.dil_artir(["C#"])
# # programci.melumatlar()


# # Ders 64 bitdi------------------------------


# # Ders 65------------------------------------

# class Calisan():

#     def __init__(self,ad,maas,departmen):
#         print("Calisanlarin init funksiyasi")

#         self.ad = ad
#         self.maas = maas
#         self.departmen = departmen
#     def melumatlar(self):
#         print("Calisanlarin melumatlari ")

#         print("Ad : {} \nMaas: {} \nDepartmen : {}".format(self.ad,self.maas,self.departmen))

#     def departmen_deyis(self,yeni_departmen):
#         self.departmen = yeni_departmen



# class Yonetici(Calisan):
#     pass


# yonetici = Yonetici("Elyane",2000,"Developer")

# yonetici.melumatlar()

# yonetici.departmen_deyis("Web Developer")


# yonetici.melumatlar()

# #-------------------------------

# class Yonetici(Calisan):
#     def zam_getir(self,zam_miqdar):
#         self.maas += zam_miqdar

# yonetici = Yonetici("Musviq",8000,"Full Stack Developer")

# yonetici.zam_getir(2000)

# yonetici.melumatlar()

# #-------------------------------


# class Calisan():

#     def __init__(self,ad,maas,departmen):
#         print("Calisanlarin init funksiyasi")

#         self.ad = ad
#         self.maas = maas
#         self.departmen = departmen
#     def melumatlar(self):
#         print("Calisanlarin melumatlari ")

#         print("Ad : {} \nMaas: {} \nDepartmen : {}".format(self.ad,self.maas,self.departmen))

#     def departmen_deyis(self,yeni_departmen):
#         self.departmen = yeni_departmen


# class Yonetici(Calisan):
#     def __init__(self, ad, maas, departmen,adam_sayi):
#         super().__init__(ad, maas, departmen)
#         print("Yonetici init funksiyasi")

#         self.adam_sayi = adam_sayi


#     def melumatlar(self):
#         print("Calisanlarin melumatlari ")

#         print("Ad : {} \nMaas: {} \nDepartmen : {}".format(self.ad,self.maas,self.departmen))

#     def departmen_deyis(self,yeni_departmen):
#         self.departmen = yeni_departmen



# yonetici = Yonetici("Musqif",2000,"Programmer",5)

# yonetici.melumatlar()

# # Ders 65 bitdi------------------------------


# # Ders 66 -----------------------------------

# class Kitab():
#     pass

# kitab = Kitab()

# print(kitab)

# # del kitab    # silir
# # print(kitab)

# #-------------------------------

# class Book():

#     def __init__(self,ad,yazar,sehife,nov):
#         print("Init funksiyasi")
#         self.ad = ad
#         self.yazar = yazar
#         self.sehife = sehife
#         self.nov = nov

# kitab = Book("Cinayet ve ceza", "Dostayevski",560,"Dram")

# #-------------------------------

# class Book():

#     def __init__(self,ad,yazar,sehife,nov):
#         print("Init funksiyasi")
#         self.ad = ad
#         self.yazar = yazar
#         self.sehife = sehife
#         self.nov = nov
#     def __str__(self):
#         return "Ad : {}\nYazar : {}\nSehife : {}\nNov :{}".format(self.ad,self.yazar,self.sehife,self.nov)


# kitab = Book("Cinayet ve ceza", "Dostayevski",560,"Dram")


# print(kitab)

# #-------------------------------

# class Book():

#     def __init__(self,ad,yazar,sehife,nov):
#         print("Init funksiyasi")
#         self.ad = ad
#         self.yazar = yazar
#         self.sehife = sehife
#         self.nov = nov
#     def __str__(self):
#         return "Ad : {}\nYazar : {}\nSehife : {}\nNov :{}".format(self.ad,self.yazar,self.sehife,self.nov)
#     def __len__(self):
#         return self.sehife

# kitab = Book("Cinayet ve ceza", "Dostayevski",560,"Dram")

# print(len(kitab))


# #-------------------------------


# class Book():

#     def __init__(self,ad,yazar,sehife,nov):
#         print("Init funksiyasi")
#         self.ad = ad
#         self.yazar = yazar
#         self.sehife = sehife
#         self.nov = nov
#     def __str__(self):
#         return "Ad : {}\nYazar : {}\nSehife : {}\nNov :{}".format(self.ad,self.yazar,self.sehife,self.nov)
#     def __len__(self):
#         return self.sehife
#     def __del__(self):
#         print("Kitab silinir...")


# kitab = Book("Cinayet ve ceza", "Dostayevski",560,"Dram")

# del kitab
# print(kitab)


# Ders 66 bitdi------------------------------


# Ders 67------------------------------------

import random
import time

class Pult():

    def __init__(self,tv_durum = "Bagli",tv_ses = 0,kanal_sirasi= ["Aztv"],kanal = "Space"):
        
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_sirasi = kanal_sirasi
        self.kanal = kanal

    def tv_ac(self):

        if(self.tv_durum == "Aciq"):
            print("Televizor zaten aciqdir")
        else:
            print("Televizor acilir...")
            self.tv_durum = "Aciq"

    def tv_bagla(self):
        
        if(self.tv_durum == "Bagli"):
            print("Televizor zaten baglidir")
        else:
            print("Televizor baglanir...")
            self.tv_durum = "Bagli"

    def ses_ayarlari(self):
        while True:
            cavab = input("Sesi azalt : '<'\nSesi artir : '>'\nCixis : cixis")

            if(cavab == "<"):
                if(self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses: ",self.tv_ses)

            elif(cavab == ">"):
                if(self.tv_ses != 31):
                    
                    self.tv_ses += 1

                    print("Ses : ",self.tv_ses)

            else:
                print("Ses guncellendi :", self.tv_ses)
                break

    def kanal_elave(self,kanal_adi):

        print("Kanal elave edilir...")
        time.sleep(1)

        self.kanal_sirasi.append(kanal_adi)

        print("Kanal elave edildi...")

    def random_kanal(self):

        ran_kanal = random.randint(0,len(self.kanal_sirasi)-1)
        self.kanal = self.kanal_sirasi[ran_kanal]

        print("Indiki kanal : ",self.kanal)

    def __len__(self):

        return len(self.kanal_sirasi)

    def __str__(self):

        return "Tv Durumu : {}\nTv Ses : {}\nKanal Listesi : {}\nIndiki Kanal : {}\n".format(self.tv_durum,self.tv_ses,self.kanal_sirasi,self.kanal)

pult = Pult()


print("""  
 Televizor Uygulamasi

 1. Tv ac
 2. Tv Bagla
 3. Ses ayarlari 
 4. Kanal elave et
 5. Kanal sayini oyren
 6. Random kanala kec
 7. Televizor melumatlari

Cixmaq ucun 'q'

 """)

while True:

    islem = input("Islemi secin : ")

    if(islem == "q"):
        print("Programdan cixdiniz")
        break

    elif (islem == "1"):
        pult.tv_ac()

    elif(islem == "2"):
        pult.tv_bagla()

    elif(islem == "3"):
        pult.ses_ayarlari()

    elif(islem == "4"):
        kanal_adlari = input("Kanal adlarini ',' ile ayirin:")

        kanal_sirasi = kanal_adlari.split(",")

        for elaveler in kanal_sirasi:
            pult.kanal_elave(elaveler)

    elif(islem == "5"):
        print("Kanal sayi : ",len(pult))

    elif(islem == "6"):
        pult.random_kanal()

    elif(islem == "7"):
        print(pult)

    else:
        print("Kecerli deyil...")










# Ders 66 bitdi------------------------------


