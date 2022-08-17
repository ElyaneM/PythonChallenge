"""
 ChallengeDay_4

"""

# Ders 46 ----------------------------------------

import re


a = [1,2,3,4,5]

a.insert(1,"Gmasnban")
print(a)     # [1, 'Gmasnban', 2, 3, 4, 5]

#--------------------------------------

a.append("Barbar")
print(a)     # [1, 'Gmasnban', 2, 3, 4, 5, 'Barbar']

#--------------------------------------

a.pop()
print(a)     # [1, 'Gmasnban', 2, 3, 4, 5]


# Ders 46 bitdi  ---------------------------------


# Ders 47 ----------------------------------------

def salamla():
    print("Salam")
    print("Necesen")

salamla()      # Salam

#--------------------------------------

def name(ad):
    print("Adin",ad)

print("Elayne")    

#--------------------------------------

def toplama(a,b,c):
    return a + b + c

print(toplama(3,4,5))


#--------------------------------------

def factorial(num):
    factorial = 1
    if(num == 0 or num ==1):
        print("Factiral",num)
    else:
        while(num >=1):
         factorial *= num
         num -= 1

        print("Faktorial",factorial)

factorial(5)    # 120


# Ders 47 bitdi  ---------------------------------

# Ders 48 ----------------------------------------

def topla(a):
    print("birinci isledi")
    return a*5

# print(topla(2,4,8))    # 14

#--------------------------------------

def vurma(a):
    print("ikinci isledi")
    return a*2
# print(vurma(3))        # 6

print(topla(vurma(5)))

# Ders 48 bitdi  ---------------------------------

# Ders 49 ----------------------------------------

def name(ad = "Ad yoxdu"):
        print("Salam",ad)

name("Elyane")

#--------------------------------------

def melumat(ad = "Yoxdur",soyad ="Yoxdur"):
    print(ad, soyad)

melumat("Elyane", "Mehiyeva")    

# Ders 49 bitdi  ---------------------------------

# Ders 50 ----------------------------------------

b = 5

def funksiya():
    print(b)

funksiya()     #5

#--------------------------------------

c = 10

def funksiya():
    c= 2
    print(c)

funksiya()    # 2
print(c)      # 10

#--------------------------------------

d = 5

def funksiya():
    global d
    d=6
    print(d)

funksiya()    # 6
print(d)      # 6

# Ders 50 bitdi  ---------------------------------

# Ders 51 ----------------------------------------

liste = [1,2,3,4,5,6]

liste1 = [i *2 for i in liste]

print(liste1)   # [2, 4, 6, 8, 10, 12]

#--------------------------------------

def vurma(a):
    return a*2
print(vurma(2))

#--------------------------------------

topla = lambda a,b : a+b
print(topla(5,2))
  
#--------------------------------------

ters = lambda text : text[::-1]
print(ters("Ters cevir"))

#--------------------------------------

tekcut = lambda num : num % 2 ==0
print(tekcut(5))

# Ders 51 bitdi  ---------------------------------

# Ders 52 ----------------------------------------

def sade(num):
    if(num == 1):
        return False

    elif(num == 2):
        return True

    else:
        for i in range(2,num):
            if(num % 2 ==0):
                return False
            return True

while True:
    num = input("Eded daxil edin : ")

    if(num == "q"):
        break
    else:
        num = int(num)

        if(sade(num)):
            print(num, "sade ededdir")   
        else:
            print(num,"sade eded deyil")

# Ders 52 bitdi  ---------------------------------

# Ders 53 ----------------------------------------

def bolenleritap(num):
        bolenler = []

        for i in range(2,num):
            if(num % i == 0):
                bolenler.append(i)

        return bolenler

while True:

    num = input("Eded daxil edin : ")   

    if(num == "q"):    
        print("Programdan cixdiniz")    
        break
    else:
          num = int(num)

          print("Bolunenler : ", bolenleritap(num))



# Ders 53 bitdi  ---------------------------------