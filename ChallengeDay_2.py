"""
    ChallengeDay_2
"""

from multiprocessing.connection import Listener


# Ders 19 ---------------------------------

liste = [12,"Hi",22]
print(liste)       #  [12, 'Hi', 22]

liste = []
print(liste)       # []

liste = list("Hello")
print(liste)       # ['H', 'e', 'l', 'l', 'o']

liste = [2,5,7,9,6,10]
print(len(liste))  # 6

print(liste[-1])   # 10

print(liste[:4])   # [2, 5, 7, 9]
print(liste[::2])  # [2,7,6]
print(liste[::-1]) # 10, 6, 9, 7, 5, 2]

liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = liste1 + liste2
print(liste3)     # [1, 2, 3, 4, 5, 6]
print(liste1*3)   # [1, 2, 3, 1, 2, 3, 1, 2, 3]
liste1 = liste1*3
print(liste1)     # [1, 2, 3, 1, 2, 3, 1, 2, 3]

liste2[1] = 10
print(liste2)     # [4, 10, 6]

print(liste)      # [2, 5, 7, 9, 6, 10]
liste[:2] = [4,8]
print(liste)      # [4, 8, 7, 9, 6, 10]
liste.append("Hello")
print(liste)      # [4, 8, 7, 9, 6, 10, 'Hello']
liste.append("Salam")
print(liste)      # [4, 8, 7, 9, 6, 10, 'Hello', 'Salam']

print(liste.pop())    # Salam
print(liste)          # [4, 8, 7, 9, 6, 10, 'Hello']
print(liste.pop(0))   # 4
print(liste)          # [8, 7, 9, 6, 10, 'Hello']


liste5 = [52,4,85,0]
print(liste5.sort())
print(liste5)        # [0, 4, 52, 85]

print(liste5.sort(reverse = True))
print(liste5)       # [85, 52, 4, 0]

liste = ["Elyane", "Azerbaycan ", "Subhan", "Melis"]
print(liste.sort())
print(liste)       # ['Azerbaycan ', 'Elyane', 'Melis', 'Subhan']
print(liste.sort(reverse = True))
print(liste)       # ['Subhan', 'Melis', 'Elyane', 'Azerbaycan ']

liste = [[1,2],[3,4],[5,6]]
print(liste)
print(liste[1][1])  # 4

liste = [1,2,3,4]
liste*3
print(liste*3)

# Ders 19 bitdi ---------------------------------------

# Ders 20 ----------------------------------------------

demet = (1,2,3,4,5,6,7)
print(demet)
print(type(demet))   # tuple

print(demet[0])      # 1

demet1 = (1,1,1,1,1,1,2,3,4)
print(demet1.count(1))  # 6
print(demet1.count(2))   # 1
print(demet1.count(10))   # 0

print(demet1.index(2))    # 6

# Ders 20 bitdi ---------------------------------

# Ders 21

luget = {"bir" :1, "iki" :2}
print(type(luget))   # dict


luget = dict()
print(luget)        # {}

luget = {"bir" :1, "iki" :2, "uc":3,"dord":4}
print(luget["bir"])  # 1

luget["bes"] = 5
print(luget)   # {'bir': 1, 'iki': 2, 'uc': 3, 'dord': 4, 'bes': 5}

luget = {'bir': [1,2,3], 'iki': [5,8,7], 'uc': [52,41,63], 'dord': [52,84,85], 'bes': [32,65,19]}
print(luget["bir"][1])   # 2


luget = {'bir': 1, 'iki': 2, 'uc': 3, 'dord': 4, 'bes': 5}
luget['bir'] = 3
print(luget)   # {'bir': 3, 'iki': 2, 'uc': 3, 'dord': 4, 'bes': 5}

luget['iki'] += 1
print(luget)         # {'bir': 3, 'iki': 3, 'uc': 3, 'dord': 4, 'bes': 5}

luget1 = {"meyveler" : {"alma":"armud","heyva":"nar"},"reqemler":{'bir':1 ,'iki': 3, 'uc': 3, 'dord': 4, 'bes': 5}}
print(luget1["reqemler"])  # {'bir': 1, 'iki': 3, 'uc': 3, 'dord': 4, 'bes': 5}

print(luget.keys())  # dict_keys(['bir', 'iki', 'uc', 'dord', 'bes'])

print(luget.values()) # dict_values([3, 3, 3, 4, 5])

print(luget.items())  # dict_items([('bir', 3), ('iki', 3), ('uc', 3), ('dord', 4), ('bes', 5)])



# jsonFormat = {
#     "user_1":{
#         "name" : "Mushvig",
#         "surname" : "Shukurov"
#     }
#     ,
#     "user_2":{
#         "name" : "Elyane",
#         "surname" : "Shukurova"
#     }
# }

# print(jsonFormat["user_1"]["name"])

# print(jsonFormat["user_2"]["name"])

# Ders 21 bitdi ------------------------------


# Ders 22 ---------------------------------

# Exercise 1

# name = input("Enter Your Name :") # Istifadeciden adini sorusduq

# message = "Welcome Back {}".format(name) # istifadeciye mesaj yaziriq amma adini format ile elave edirik

# print(message) # mesaji ekrana yaziriq

# Exercise 2

# a = int(input("Eded daxil edin"))

# b = int(input("2 ci ededi daxil edin"))

# c = a + b

# print(c)

# print(input("Bir eded daxil et"))

# num = int(input("Eded daxil et :"))
# print(num*3)

# number = int(input("Eded daxil et :"))
# print("Daxil etdiyiniz eded: ",number)

# a = int(input("birinci ededi daxil edin :"))
# b = int(input("ikinci ededi daxil edin :"))
# c = int(input("ucuncu ededi daxil edin :"))
# print("Cem", a+b+c)
# Ders 22 bitdi ---------------------------------------

# Ders 23 ---------------------------------------
# print("Telebe haqqinda melumat yazin")

# ad = input("Telebenin adi : ")
# soyad = input("Telebenin soyadi : ")
# qrup = input("Telebenin oxudugu qrup : ")

# melumatlar = [ad,soyad,qrup]
# print("Melumat yadda saxlanilir........")

# print("Telebenin adi : {}\n Telebenin soyadi : {}\n Telebenin oxudugu qrup : {}".format(melumatlar[0],melumatlar[1],melumatlar[2]))

# print("Melumat saxlanildi...")


# Ders 23 bitdi ------------------------------


# Ders 26 ----------------------------------


print(type(True))  # bool

print(bool(1))     # True
print(bool(0))     # False

print(1==1)        # True
print(1==2)        # False

print("Elyane" == "Elyane")  # True

print(2>4)             # False
print("Mushvig" > "Elyane")  # True

# Ders 26 bitdi -------------------------------

# Ders 27 ----------------------------------


print(2<5 and "Elyane" == "Elyane")     # True


print(5==6 and 6==6)       # False

print(2>1 and 5==5 and "Abd" == "Abd")  # True

print(5==6 or 6==6)    # True
print(2>1 or 5==5 or "Abd" == "Abd")   # True
print(1>2 or 'Hello' != 'Hello')       # False

print(not 2==2)         # False

print("Canberk" < "Oğuz")  # True
print("Elyane" < "Mushvig") # True

# Ders 27 bitdi --------------------------

# Ders 28 ---------------------------------

a=2
if(a==2):
    print(a)

# yas = int(input("Yasini yaz : ")) 
# if yas < 18:
#     print("Olmaz")   
# else:
#     print("Olar")    

# Ders 28 bitdi ---------------------------------

# Ders 29 ------------------------------------

# num = input("Eded daxil edin")

# if num == "1":
#     print("Tamamdir")
# elif num == "2":
#     print("OLur")
# elif num == "3":
#     print("Hadi")
# else:
#     print("Olmaz")

# Ders 29 bitdi --------------------------------

# Ders 30 -------------------------------
 
# a = int(input("Ededi daxil et : "))
# b = int(input("Ededi daxil et : "))

# hesab = input("Hesablayin : ")

# if(hesab == "1"):
#     print("{} {} cemi {}".format(a,b,a+b))
# elif(hesab == "2"):
#     print("{} {} ferqi {}".format(a,b,a-b))
# elif(hesab == "3"):
#     print("{} {} hasili {}".format(a,b,a*b))
# elif(hesab == "4"):
#     print("{} {} qismeti {}".format(a,b,a/b))
# else:
#     print("Sehvdir")

# Ders 30 bitdi --------------------------------

# Ders 31

istifadeci_adi = "Elyane"
sifre = "1235"

adi = input("Ad daxil edin : ")
parol = input("Parolu daxil edin :")

if istifadeci_adi == adi and sifre != parol:
    print("Sifre sehvdir")
elif istifadeci_adi != adi or sifre == parol:
    print("Ad sehvdir")
else:
    print("Daxil ola bilersiniz")

# Ders 31 bitdi ------------------------
