from calendar import c
import re
from Module.giris import start
start(9)


#------------------------------------
import datetime
class VehicleRent:

    def __init__(self,stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        print("{} masin var hazirda".format(self.stock))
        return self.stock

    def rentHourly(self,n):
        if n <= 0 :
            print(") ve ya menfi ola bilmez !!!")
            return None
        elif n > self.stock:
            print("Uzgunuz,{} sayisinda masin qalmamis ... ".format(self.stock))
        else:
            self.now = datetime.datetime.now()
            print("Saat {} ucun {} neqliyyat qalmayib".format(self.now.hour,n))

            self.stock -= n
            return self.now

    def rentDaily(self,n):
         if n <= 0 :
            print(") ve ya menfi ola bilmez !!!")
            return None
         elif n > self.stock:
            print("Uzgunuz,{} sayisinda masin qalmamis ... ".format(self.stock))
         else:
            self.now = datetime.datetime.now()
            print("Bu {} gun ucun {} neqliyyat qalmayib".format(self.now.hour,n))

            self.stock -= n
            return self.now

    def returnVehicle(self,request,brand):
        
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle

                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle

                if (2 <= numOfVehicle):
                    print("20% endirim edirik sene ")
                    bill = bill*0.8

                print("Bize muraciet etdiyiniz ucun tesekkurler !!!")
                print("Qiymet : {}".format(bill))
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle

                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle

                if (4 <= numOfVehicle):
                    print("20% endirim edirik sene ")
                    bill = bill*0.8

                print("Bize muraciet etdiyiniz ucun tesekkurler !!!")
                print("Qiymet : {}".format(bill))
                return bill

        else:
            print("Bele sey yoxdu bizde")
            return None

class CarRent(VehicleRent):
    
    global discount_rate
    discount_raten = 15


    def __init__(self,stock):
        super().__init__(stock)

    def discount(self,b):
       bill = b - (b*discount_rate)/100
       return bill


class BikeRent(VehicleRent):

    def __init__(self, stock):
        super().__init__(stock)


class Customer:

    def __init__(self):
        
        self.bikes = 0
        self.rentaBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentaBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self,brand):
        
        if brand == "bike":
            bikes == input("Nece velik kiraye goturmek isteyirsiniz? ")

            try:
                bikes = int(bikes)
            except ValueError:
                print("nomre olmalidir")
                return -1

            if bikes < 1:
                print("0 olmamalidir")
                return -1
            else:
                self.bikes = bikes
            return self.bikes
        
        elif brand == "car":
            cars == input("Nece masin kiraye goturmek isteyirsiniz? ")
          
            try:
              cars = int(cars)
            except ValueError:
                print("nomre olmalidir")
            return -1

            if cars < 1:
                print("0 olmamalidir")
                return -1
            else:
                self.cars = cars
            return self.cars

        else:
            print("xeta var")
     

    def returnVehicle(self,brand):
        
        if brand == "bike":
            if self.rentalTime_b and self.rentaBasis_b and self.bikes:
                return self.rentalTime_b, self.rentaBasis_b, self.bikes
            else:
                return 0,0,0

        elif brand == "cars":
            if self.rentalTime_c and self.rentaBasis_c and self.cars:
                return self.rentalTime_c, self.rentaBasis_c, self.cars
            else:
                return 0,0,0
        else:
            print("Error var")



bike = BikeRent()
car = CarRent()
customer = Customer()

main_menu = True

while True:

    if main_menu :
        print(""" 
        ****Vehicle Rental Shop****
        A. Bike Menu
        B. Car Menu
        Q. Exit
        """)
        main_menu = False

        choice = input("Sec : ")

    if choice == "A" or choice == "a":

        print("""
            ****Velik Menyu****
            1. Velikleri goster
            2. Bir saati 5$ olan velikler
            3. Gunu 84$ olan velikler
            4. Veliki qaytar
            5. Menu
            6. Cix
        """)

        choice = input("Sec : ")

        try:
            choice = int(choice)
        except ValueError:
            print("Bele sey yoxdu")
            continue

        if choice == 1:
            bike.displayStock()
            choice == "A"

        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentaBasis_b = 1
            main_menu = True
            print("----------------")

        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle(bike))
            customer.rentaBasis_b = 2
            main_menu = True
            print("----------------")

        elif choice == 4:
            customer.bill =  bike.returnVehicle(customer.requestVehicle("bike"),"bike")
            customer.rentaBasis_b, customer.rentalTime_b,customer.bikes = 0,0,0
            main_menu = True

        elif choice == 5:
            main_menu = True

        elif choice == 6:
            break

        else:
            print("Bele secenek yoxdu")
            main_menu = True

    elif choice == "B" or choice == "b":

        print("""
            ****Car Menyu****
            1. Masinlari goster
            2. Bir saati 5$ olan masinlar
            3. Gunu 84$ olan masinlar
            4. Masini qaytar
            5. Menu
            6. Cix
        """)

        choice = input("Sec : ")

        try:
            choice = int(choice)
        except ValueError:
            print("Bele sey yoxdu")
            continue

        if choice == 1:
            car.displayStock()
            choice == "B"

        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("Car"))
            customer.rentaBasis_c = 1
            main_menu = True
            print("----------------")

        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentaBasis_c = 2
            main_menu = True
            print("----------------")

        elif choice == 4:
            customer.bill = car.returnVehicle(customer.requestVehicle("car"),"car")
            customer.rentaBasis_c, customer.rentalTime_c,customer.cars = 0,0,0
            main_menu = True

        elif choice == 5:
            main_menu = True

        elif choice == 6:
            break

        else:
            print("Bele secenek yoxdu")
            main_menu = True


    elif choice == "Q" or choice == "q":
        break

    else:
        print("Duzgun secin!!!")

    print("Bizi secdiyiniz ucun tesekkurler <3")