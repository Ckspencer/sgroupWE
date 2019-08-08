print("Welcome to the meeting room booking system!")
print(" ")

print("Do you want to check for any bookings? (Y/N)")
if input()== "Y":
        Name = input("Please enter your name: ")

        if Name in open('MeetingRoom.txt').read():
                print("You have a booking!")
        else:
                print("No booking was detected.")

print("Do you want to make a booking? (Y/N)")
if input()== "Y":
        Name = input("Please enter your name: ")       
        while True:
            try:
                Room = int(input("Select a room from [1-4]: "))
                break
            except:
                print("That's not a valid option!")

        if Room == 1:
            print("You have Chosen room 1")
        elif Room == 2:
            print("")
        elif Room == 3:
            print("")
        elif Room == 4:
             print("")
        else:
            print('invalid Input!')

        SDate = input("Input a date when the meeting will start, with the format [D/M/YEAR]: ")
        EDate = input("Input a date when the meeting will end, with the format [D/M/YEAR]: ")
        STime = input("Input a time when the meeting will start, with the format [Hr/min]: ")
        ETime = input("Input a time when the meeting will start, with the format [Hr/min]: ")
else:
        exit()

Booking =[Name,Room,SDate,EDate,STime,ETime]

with open('MeetingRoom.txt','w') as f:
 for item in Booking:
  f.write("%s\n" % item)
print(" ")
print("Room " + (Room) + " is now booked by " + (Name) + " on the " + (SDate) + " at " + (STime) + " until the " + (EDate) + " at " + (ETime))
