class PassengerRegistration():
    def __init__(self, passengerName, num_of_passengers,destination_location, departure_location, select_Bus_type ):
      self.passengerName = None
      self.num_of_passengers = None
      self.destination_location = None
      self.departure_location = None 
      self.ddmmyy= None
      self.seat_num = None
      self.select_Bus_type = None
      self.bus_fare = None
      self.autoInc = 1 
      self.countcol = 0 
    
    def getPassengerInfo(self):
        self.passengerName = input("Enter Passenger Name:")
        self.num_of_passengers = int(input("Enter Number of Passenger: "))
        print("Please choose your trip")
        print("1. Gaza Governate")
        print("2. North Gaza Governate")
        print("3. Middle Gaza Governate")
        print("4. South Gaza Governate")

        self.d1 = int(input("Enter Departure Location"))
        if self.d1 ==1:
            self.departure_location = "Gaza Governate"
        elif self.d1==2:
            self.departure_location= "North Gaza Governate"
        elif self.d1==3:
            self.departure_location= "Middle Gaza Governate"
        elif self.d1 ==4:
            self.departure_location= "South Gaza Governate"
        else:
            print("Please enter a valid location and try agian!")
        
        print("1. Alremal street")
        print("2. Bet Hanon")
        print("3. Alzwayda")
        print("4. Jala street @ Khanyounis")

        self.dp1 = int(input("Enter Destination Location: "))
        if self.dp1 == 1:
            self.destination_location = "Alremal street"
        elif self.dp1 == 2:
            self.destination_location = "Bet Hanon"
        elif self.destination_location == 3:
            self.destination_location = "Alzwayda"
        elif self.destination_location == 4:
            self.destination_location = "Jala street @ Khanyounis"
        else:
            print("Try another valid location") 
        
        self.ddmmyy = input("Enter Date of Joiurney Like 07-29-2022: ")

        print("[1] [2] [3] [4] [5] [6] [7] [8] [9] [10]")
        print("[11] [12] [13] [14] [15] [16] [17] [18] [19] [20]")
        print("[21] [22] [23] [24] [25] [26] [27] [28] [29] [30]")
        print("[31] [32] [33] [34] [35] [36] [37] [38] [39] [40]")
        print("[41] [42] [43] [44] [45] [46] [47] [48] [49] [50]")

        seat_Num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        self.bookinglist = []
        while(True):
            self.seat_num = int(input("Choose a seat number [Note: you can book two tickets as max.]: "))
            if self.seat_num <=30:
                if self.seat_num in seat_Num_list:
                    self.bookinglist.append(self.seat_num)
                    del seat_Num_list[self.seat_num +1]
                    count = len(seat_Num_list)
                else:
                    print("Ticket Allready Booked")
                    print("Do You Want To Book One More Seat Enter (Yes/No)")
                    y = input(" ")
                    if y == "Yes":
                        pass
                    else:
                        break
            else:
                print("Choose a Seat Number Which is Available")
        
        print("1. Air-conditioned bus:[Fare = 3 NIS]")
        print("2. Non air-conditioned bus: [Fare = 2 NIS]")
        self.select_Bus_type = int(input("Select your bus: "))

        if self.select_Bus_type == 1:
            self.select_Bus_type = "Air-conditioned bus"
            self.bus_fare = self.num_of_passengers * 3
        elif self.select_Bus_type == 2: 
            self.select_Bus_type = "Non air-conditioned bus"
            self.bus_fare = self.num_of_passengers * 2 






    


