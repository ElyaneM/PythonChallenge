"""
 ChallengeDay_3

"""

# Ders 35-----------------------------------------------------------------

from math import factorial


print(5 in [1,2,3,4])         # False
print("p" in "python")        # True
print(not 1 in [2,3,4])       # True

liste = [1,2,3,4,5,6,7]

for i in liste:
    print(i)    # 1 2 3 4 5 6 7

sum = 0
for i in liste:
    sum += i
print(sum)      # 28


#-------------------------------------------
name = "Elyane"
nameArray = list(name)

herfler = ""

for herf in nameArray:
    herfler+=herf

print(herfler)
#--------------------------------------------

start = 0
reqemler = ""
while start<100:
    reqemler+=str(start)
    start+=1

print(reqemler)
#--------------------------------------------

liste = [1,2,3,4,5,6,7]

for i in liste:
    if i % 2 == 0:
        print(i)      # 2 4 6

#--------------------------------------------

name = "Elyane"

for i in name:
    print(i * 3)
# EEE
# lll
# yyy
# aaa
# nnn
# eee


#--------------------------------------------

liste = [(1,2),(3,4),(5,6),(7,8)]

for (i,j) in liste:
    print("i : {} j : {}".format(i,j))
# i : 1 j : 2
# i : 3 j : 4
# i : 5 j : 6
# i : 7 j : 8

#--------------------------------------------

luget = {"bir" : 1, "iki" : 2, "uc" : 3}

for i in luget.values():
    print(i)            # 1 2 3

for i in luget.keys():
    print(i)            # bir iki uc

# Ders 35 bitdi ---------------------------------------------

# Ders 36 ---------------------------------------------------

# --------------------------------------------------
i = 0
while (i<10):
    print(i)
    i+=1 


a = 1
while (a<20):
    print(a)
    a+=2 

# --------------------------------------------------

name = 0

while name<5:
    print("Elyane")
    name +=1

# --------------------------------------------------

liste = [1,2,3,4,5,6,7]

index = 0
while (index<len(liste)):
    print(index,liste[index])
    index+=1


# Ders 36 bitdi--------------------------------------------------

# Ders 37 -------------------------------------------------------

print(*range(0,10))         # 0 1 2 3 4 5 6 7 8 9

print(*range(0,15,2))       # 0 2 4 6 8 10 12 14

print(*range(10,0,-1))      # 10 9 8 7 6 5 4 3 2 1

# --------------------------------------------------

for i in range(1,11):
    print(i)

# --------------------------------------------------

# for i in range(1,10):
#     print("E " * 1)


# Ders 37 bitdi -----------------------------------------------

# Ders 38 -----------------------------------------------------

print("************Ders38*******************")
i = 0
while (i<10):
    i+=1
    if( i == 5 ):   
        break
    print(i)

# --------------------------------------------------

# name = input("Ad daxil et (Bitirmek ucun : 'q')")

# while True:
#     name = input("Ad daxil et (Bitirmek ucun : 'q')")
#     if (name == "q"):
#         print("Programdan cixdin")
#         break
#     print(name)


# --------------------------------------------------

i = 0

while (i<10):
    i+=1
    if(i==3 or i == 5):
        continue
    print(i)
# Ders 38  bitdi--------------------------------------------------


# Ders 39  -------------------------------------------------------

liste = [1,2,3,4,5,6,7]

liste2 = list()

for i in liste:
    liste2.append(i)
print(liste2)      # [1, 2, 3, 4, 5, 6, 7]

# --------------------------------------------------

liste = [1,2,3,4,5,6,7]

liste3 = [i for i in liste]
print(liste3)         # [1,2,3,4,5,6,7]

# --------------------------------------------------

# Videonun sonunu basa dusmedim



# Ders 39  bitdi--------------------------------------------------



# Ders 40  -------------------------------------------------------

# name = "Elyane"
# parol = "1254"
# haqq = 3
# while True:
#     adi = input("Adi daxil edin : ")
#     sifre = input("Kodu daxil edin: ")
#     if(adi == name and sifre != parol):
#         print("Kod sehvdir")
#         haqq-=1
#     elif(adi != name and sifre == parol):
#         print("Ad sehvdir")
#         haqq -=1
#     elif(adi != name and sifre != parol):
#         print("Ad ve kod sehvdir") 
#         haqq-=1
#     else:
#         print("Xosgeldin")
#         break
#     if(haqq == 0):
#         print("Giris haqqin bitdi")
#         break

# Ders 40 bitdi  -----------------------------------------------------
# Ders 41 ------------------------------------------------------------


# 1: Hesabini yoxla
# 2: Pul yatir
# 3: Pul cek

# hesab = 2000

# while True:
#     islet = input("Islemi secin")

#     if(islet  == "q"):
#         print("Hesabdan cixdin")
#         break
#     elif(islet == "1"):
#         print("Hesabiniz {} manatdir".format(hesab))
#     elif(islet == "2"):
#        miqdar = int(input("Hesaba pul yatir"))
#        hesab+=miqdar
#     elif(islet == "3"):
#         miqdar = int(input("Pulu miqdarini yaz"))
#         if(hesab - miqdar < 0):
#             print("O qeder pul yoxdu")
#             continue
#         hesab -= miqdar
#     else:
#         print("Gecersiz")



# Ders 41 bitdi  -----------------------------------------------------


# Ders 42 ------------------------------------------------------------

# while True:
#     num = input("Reqem daxil edin : ")
#     if(num == "q"):
#         print("Programdan cixdiniz")
#         break
#     else:
#          num = int(num)

#          factorial = 1
#          for i in range(2,num+1):
#             print("Fakorial",factorial, "i :", i)
#             factorial *=i
#             print("Fakorial ",factorial)


# Ders 42 bitdi  -----------------------------------------------------

# Ders 43 ------------------------------------------------------------

a = 1
b=1
fibonacci = [a,b]
for i in range(10):
    a,b = b, a+b
    fibonacci.append(b)
print(fibonacci)        # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]





# Ders 43 bitdi  -----------------------------------------------------

