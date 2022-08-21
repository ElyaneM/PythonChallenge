import re
from Module.giris import start
start(12)


# Bolum 11---------------------------------
# Map
# def double(x):
#     return x * 2

# new = map(double,[1,2,3,4,5,6])
# for i in new:
#     print(i)

# new = list(new)
# print(new)

# mapimiz = map(lambda x : x ** 2,(1,2,3,4,5))


# print(list(mapimiz)) 

#------------------------------------------------

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# arr3 = [3,5,8,6]

# vurma = map(lambda x,y : x * y, arr1, arr2)

# print(list(vurma))

# vurma = map(lambda x,y,z : x * y * z, arr1, arr2, arr3)

# print(list(vurma))

#------------------------------------------------

# Reduce

from functools import reduce

def toplama(x,y):
    return x+y

print(reduce(toplama,[12,45,85,96]))

print(reduce(lambda x,y : x*y,[1,2,3,4,5]))

#------------------------------------------------

def maximum(x,y):
    if(x>y):
        return x
    else:
        return y

print(maximum(2,6))

print(reduce(maximum,[2,5,8,46]))


#------------------------------------------------

# Filter

fil = filter(lambda x : x % 2 == 0, [1,5,7,6,4])

print(fil)

print(list(fil))


def sade_eded(x):
    i = 2

    if(x == 1):
        return False
    elif (x == 2):
        return True
    else:

        while(i < x):

            if (x % i == 0):
                return False
            i += 1
        return True

print(sade_eded(6))

print(list(filter(sade_eded,range(1,100))))
    
#------------------------------------------------

# Zip

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]

print(zip(liste1,liste2))

liste = zip(liste1,liste2)

print(list(liste))    # [(1, 5), (2, 6), (3, 7), (4, 8)]

for i,j in zip(liste1,liste2):
    print(i,j)

sozler1 = {"Alma" : 1, "Armud" : 2, "Heyva" : 3}
sozler2 = {"Bir" : 4 , "Iki" : 5, "Uc" : 3}

print(list(zip(sozler1,sozler2)))  # [('Alma', 'Bir'), ('Armud', 'Iki'), ('Heyva', 'Uc')]
print(list(zip(sozler1.values(),sozler2.values())))  # [(1, 4), (2, 5), (3, 3)]


#------------------------------------------------

# Enumerate 

arr = ["Emilya" , "Sebnem", "Seadet", "Arzu", "Gunel"]

print(list(enumerate(arr)))  # [(0, 'Emilya'), (1, 'Sebnem'), (2, 'Seadet'), (3, 'Arzu'), (4, 'Gunel')] 

for i,j in enumerate(arr):
    print(i,j)

elifba = ["a", "b", "c", "d","e", "f"]

for i,j in enumerate(elifba):
    if i % 2 == 0:
        print(j)   # a c e

#------------------------------------------------

# All and any

def hamisi(liste):
    for i in liste:
        if not i :
            return False

    return True

liste = [True, False, True]

print(hamisi(liste))    # False

arr = [1,2,3,6]
print(hamisi(arr))    # True

def hansisa(liste):
    for i in liste:
        if i :
            return True
    return False

print(hansisa([True, False, True]))   # True

arr = [0,0,0,0,0,0]

print(hansisa(arr))   # False


print(all([True, False, True]))    # False

print(all([True, True,True]))      # True
print(all([False, False,False]))      # False


print(any([True, False, True]))   # True
print(any([True, True,True]))   # True
print(any([False, False,False]))   # TFalse


