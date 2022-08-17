from __future__ import division
from calendar import Calendar
import re
from sqlite3 import adapt
from xml.dom import pulldom
from Module.giris import start
start(8)

# class Calc(object):

#     def __init__(self,a,b):

#         self.value1 = a
#         self.value2 = b

#     def add(self):

#         return self.value1 + self.value2

#     def multyply(self):
        
#         return self.value1 * self.value2
    
#     def division(self):

#         return self.value1 / self.value2

# selection = input("select 1 or 2 or 3 :")

# v1 = int(input("ilk eded : "))
# v2 = int(input("2ci eded : "))

# c1 = Calc(v1,v1)

# if selection == "1":
#     add_result = c1.add()
#     print("Add : {}".format(add_result))

# elif selection == "2":
#     muliply_result_ = c1.multyply()
#     print("Multiply : {}".format(muliply_result_))

# elif selection == "3":
#     division_result = c1.division()
#     print("Division : {}".format(division_result))

#-----------------------------------------

class Bank(object):

    def __init__(self,ad,pul,adress):
         self.ad = ad
         self.__pul = pul
         self.adress = adress

    def getMoney(self):
        return self.__pul

    def setMoney(self,miqdar):
        self.__pul = miqdar

    def __increase(self):
        self.__pul = self.__pul + 500


p1 = Bank("Musqif",10000,"Xirdala")
p2 = Bank("Elyane",5000,"Sahil")

# print(p1.ad)
# print(p1.__pul)

# print("get methodu : ", p1.getMoney())

# p1.setMoney(5000)

# print("Sonraki pul : ", p1.getMoney())

# p1.__increase()
# print("Artirilmis pul : ",p1.getMoney())


#-----------------------------------------

class Animal:
    def __init__(self):
        print("Heyvan yaradildi")

    def toString(self):
        print("heyvan")

    def walk(self):
        print("heyvan qacir")


class Meymun(Animal):
    def __init__(self):
        super().__init__()
        print("Meymun yaradildi")

    def toString(self):
        print("meymun")

    def climb(self):
        print("Meymun hoppanir")


class Qus(Animal):
    def __init__(self):
        super().__init__()
        print("Qus yaradildi")

    def fly(self):
        print("Qus ucur")


m1 = Meymun()
m1.toString()
m1.walk()

b1 = Qus()
b1.fly()
b1.walk()


#-----------------------------------------

class Website:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " " + self.surname)


class Website1(Website):
    def __init__(self, name, surname,ids):
        Website.__init__(self,name, surname)
        self.ids = ids
    
    def login(self):
        print(self.name +" " + self.surname + " " + self.ids)


class Website2(Website):
    def __init__(self, name, surname,email):
        Website.__init__(self,name, surname)
        self.email = email

    def login(self):
        print(self.name +" " + self.surname + " " + self.email)



p1 = Website("Elyane","Mehiyeva")
p2 = Website1("Subhan", "Mehiyev","1234")
p3 = Website2("Subhan", "Mehiyev","supus@gmail")
print(p3.login())


#-----------------------------------------

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def walk(self): pass

    def run(self): pass

class Bird(Animal):

    def __init__(self) :
        print("Qus")

    def walk(self):
        print("walk")

b1 = Bird()


#-----------------------------------------

class Animal:

    def toString(self):
        print("heyvan")


class Monkey:

    def toString(self):
        print("meymun")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString()


#-----------------------------------------

class Employee():

    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print(result)

class CompEng(Employee):

    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print(result)

class EEE(Employee):

    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print(result)

e1 = Employee()

ce = CompEng()

eee = EEE()

employee_list = [ce,eee]

for employee in employee_list:
    employee.raisee()