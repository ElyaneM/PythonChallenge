import re
from Module.giris import start
start(10)

#----------------------------------

# a = int("asvhcsdaj246328200")

# try:
#     a = int("asvhcsdaj246328200")
#     print("Program isledi")
# except:
#     print("Programda xeta var")
# print("Program bitdi")

#--------------------------------

# try:
#     a = int("246328200")
#     print("Program isledi")
# except:
#     print("Programda xeta var")
# print("Program bitdi")

#--------------------------------"

# try:
#     a = int("asvhcsdaj246328200")
#     print("Program isledi")
# except ValueError:
#     print("Programda xeta var")
# print("Program bitdi")

#--------------------------------


# try :
#     a = int(input("Birinci ededi yazin : "))
#     b = int(input("Ikinci ededi yazin : "))
#     print(a/b)
# except ValueError:
#     print("Ancaq reqem daxil edin!!!")
# except ZeroDivisionError:
#     print("0 -a bolmek olmur!!!")
# print("Program bitdi...")

#--------------------------------

# try :
#     a = int(input("Birinci ededi yazin : "))
#     b = int(input("Ikinci ededi yazin : "))
#     print(a/b)
# except (ValueError,ZeroDivisionError):
#     print("ValueError ve ya ZeroDivisionError var")
# print("Program bitdi...")
    

#--------------------------------

# try :
#     a = int(input("Birinci ededi yazin : "))
#     b = int(input("Ikinci ededi yazin : "))
#     print(a/b)
# except ValueError:
#     print("Ancaq reqem daxil edin!!!")
# except ZeroDivisionError:
#     print("0 -a bolmek olmur!!!")
# finally:
#     print("Isleyir...")
# print("Program bitdi...")

#--------------------------------

def terscevir(s):
    if(type(s) != str):
        raise ValueError("String daxil edin!!!")
    else:
        return s[::-1]

print(terscevir("Elyane"))
# print(terscevir(12))

#--------------------------------

# arr = range(0,100,10)
# print(*arr)

# for num in arr:
#     print(num)

#--------------------------------

def RangeM(start,end,step = 1):
    arr = []
    if(start < end):
        while start < end:
            arr.append("{} ".format(str(start)))
            start += step
    elif(start>end and step<0):
        while start>end:
            arr.append("{} ".format(str(start)))
            start += step
    return "".join(arr)

arr = RangeM(100,0,-1)
# arr = RangeM(0,100,10)

print(arr)