from passenger_details import* 
p_name = input("Enter passenger name:")
p_password = int(input("Enter your password: "))
c_number = int(input("Enter passenger number: "))


class busstation:
    p_name = ""
    p_password = 0
    p_number = 0 
    passengers = [None]*c_number
    num_of_passengers=0

    def addpassenger(self,passengers):
        passenger_Name = input("Enter your name: ")
        num_of_passengers = int(input("Enter the number of passengers: "))
        destination_location = input("Enter your destination: ")
        departure_location = input("Enter your departure location: ")
        select_bus_type = int(input("Enter bus type: "))
        p = PassengerRegistration(passenger_Name, num_of_passengers, destination_location, departure_location, select_bus_type )
        passengers[busstation.passengers]=p 
        busstation.num_of_passengers+=1 
        print("Passenger data:", p.passengerName(), p.num_of_passengers(), p.departure_location(), )
    
    
    def bookSeat(self,passengers):
        seat_num= int(input("Choose your Seat:"))
        found=0
        for n in range(busstation.passengers):
            if(seat_num==passengers[n].getseat_num()):
                print("Your seat number is:", passengers[n].getseat_num())
                found=1 
        if(found==0):
            print("The seat you ahve entered is not available!")
    

    def display(self,passengers):
        if (busstation.passengers==0):
            print("There is no seats booked yet")
        else:
            for n in range(busstation.passengers):
                print("The seats in the bus are:", passengers[n].getseat_num())
    

def menu():
     print("1. Add passenger data")
     print("2. Make a new book")
     print("3. Display all seats")
     print("4. quit")
     global choice
     choice=int(input("Enter your choice"))


g = busstation() 

while(True):
    menu()
    if(choice==1):
        g.addpassenger(g.passengers)
    elif(choice==2):
        g.bookSeat(g.passengers)
    elif(choice==3):
        g.display(g.passengers)
    elif(choice==4):
        print("Thank You!")
        break
    else:
        print("Invalid input!") 








