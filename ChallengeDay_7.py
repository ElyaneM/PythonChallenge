from re import I
from unittest import result
from Module.giris import start
start(7)

#------------------------------------

class Telebe():

    ad = "Elyane Mehiyeva"
    yas = "21"

telebe = Telebe()

print(telebe)

print(telebe.ad)
print(telebe.yas)

#------------------------------------


class Square():

    teref = 5
    area = 0
    def area1(self):
        self.area = self.teref * self.teref

        print(self.area)

s1 = Square()

print(s1)
print(s1.teref)
print(s1.area1())

s1.teref = 7
print(s1.area1())


#------------------------------------

class Emp():

    yas = 25
    maas = 5000  # $

    def hesabla(self):
        a = self.yas/self.maas
        print(a)

def hesabla(yas,maas):
    a = yas/maas
    print(a)

e1 = Emp()
e1.hesabla()

#------------------------------------

def findArea(pi,r):
    area = pi*r**2
    # print(area)
    return area

pi = 3.14
r = 5

result1 = findArea(pi,r)
print(result1)
result2 = findArea(pi,10)
print(result1 + result2)


