from Module.giris import start
start(11)


# Bolum 10 ----------------------------------

# file =  open("bilgi.txt","w",encoding="utf-8")

# file.write("Elyanə Məhiyeva")
# file.write(" Şükürova\n")


# file =  open("bilgi.txt","a",encoding="utf-8")

# file.write("Mesajimi almistir o\n")


# file.close()

try:
    file = open("bilgiler2.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("File tapilmadi")


file = open("bilgiler2.txt","w",encoding="utf-8")

file.write("Sübhan\n")
file.write("Əntiqə\n")
file.write("Məlahət\n")
file.write("Mehriban\n")
file.write("Eyvaz\n")

file = open("bilgiler2.txt","r",encoding="utf-8")


for i in file:
    print(i, end ="")
file.close()

file = open("bilgiler2.txt","r",encoding="utf-8")

read = file.read()

print(read)


file = open("bilgiler2.txt","r",encoding="utf-8")

print(file.readline())   # tek setir oxuyur
file.close()


file = open("bilgiler2.txt","r",encoding="utf-8")

file.readlines()
liste = file.readlines()
print(liste)
file.close()   # islemedi


#--------------------------------------

with open("bilgiler2.txt","r", encoding="utf-8") as file:
    print(file.tell())


with open("bilgiler2.txt","r", encoding="utf-8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell())
#--------------------------------------


with open("bilgiler2.txt","r", encoding="utf-8") as file:
    file.seek(5)
    print(file.tell())   # 5
    print(file.read(10))

#--------------------------------------

with open("bilgiler2.txt","r", encoding="utf-8") as file:
    file.seek(0)
    print(file.read(6))

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    print(file.read())

#--------------------------------------

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    file.seek(5)
    file.write("kakbsc")
    print(file.read())

#--------------------------------------

with open("bilgiler2.txt","a", encoding="utf-8") as file:
    file.write("Natix")
    

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    print(file.read())

#--------------------------------------

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    elave = file.read()
    elave = "Ehtiram\n" + elave
    file.seek(0)
    file.write(elave)  

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    print(file.read())    

#--------------------------------------

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)

with open("bilgiler2.txt","r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Zaur\n")
    print(liste)

