import datetime

#------\------\------\------MainMenu------/------/------/------#

def MainMenu():
#------\User-Interface/------#    
    print("Welcome to the meeting room booking system!\n")
    while True:                             # MainMenu via while loop / User is presented with four options (1-4)
        print("---//--/-Menu-\--\\---")
        print("[1] Exit Program")           # Program ends
        print("[2] Add Booking")            # User can add a booking
        print("[3] Remove Booking")         # User can remove a booking
        print("[4] Check Room Bookings")    # User can check room bookings
        try:
            userinput = int(input("Please select an option (0-4):")) 
            if not 0 <= userinput <= 4:     #Only allows it to be in range of 1-4
                raise ValueError
        except ValueError:                  # If anything else is inputed then 1-4,
            print("\nInvalid Number\n")     # It shall detect it as a invalid number
        if userinput == 1:                  # Option 1 - kill's the program
            print("\nThank you for using the meeting room booking system!")
            exit()
        elif userinput == 2:                                # Option 2 redirects to the BookRoom Function.
            BookRoom()
        elif userinput == 3:                                # Option 3 redirects to the DeleteRoom Function.
            DeleteRoom()
        elif userinput == 4:                                # Option 4 redirects to the GetUserBookedRooms.
            GetUserBookedRooms()
            
#------\------\------\------BookRoom------/------/------/------#
            
def BookRoom():                                             # User must input Name, Room #, Start/End #, Start/End
    from datetime import date                               # Name is taken from userinput
    today = date.today()                                    # Room is taken from userinput
    print("Today's date is", today)
    name = input("Please enter your name:\n")
    room = input("Select a Room [1-4]:\n")

#------\StartTime/------#

    startdate_entry = input("Input a date when the meeting will start, with the format of [DD/MM/YY]:\n")
    day, month, year = map(int, startdate_entry.split("/"))
    ValidDateCheck = True
    try :
        datetime.datetime(int(day),int(month),int(year))
    except ValueError :
        ValidDateCheck = False

    if(ValidDateCheck) :
        print ("Valid date")
        pass
    else :
        print ("Invalid Date, make sure dates are in range\n")
        BookRoom()
                                                            
    starttime_entry = input("Select a time when the meeting will start, with the format of [HH:MM]:\n")
    hour, minute = map(int, starttime_entry.split(":"))
    
    starttime = datetime.datetime(year, month, day, hour, minute) # This information is compiled into a single list and then written...

#------\EndTime/------#

    enddate_entry = input("Input a date when the meeting will end, with the format of [DD/MM/YY]:\n")
    day, month, year = map(int, enddate_entry.split("/"))
    ValidDateCheck = True
    try :
        datetime.datetime(int(day),int(month),int(year))
    except ValueError :
        ValidDateCheck = False

    if(ValidDateCheck) :
        print ("Valid date")
        pass
    else :
        print ("Invalid Date, make sure dates are in range\n")
        BookRoom()
                                        
    endtime_entry = input("Select a time when the meeting will end, with the format of [HH:MM]:\n")
    hour, minute = map(int, endtime_entry.split(":"))

    endtime = datetime.datetime(year, month, day, hour, minute)
    
#------\StartTime + EndTime/------#

    booking = [name, room, starttime, endtime]
    with open('MeetingRoom.txt', 'a') as f:                 # Allows IDLE too find the txt file location.
        for item in booking:                                # Outputed to a text file in one line, where the types are split by spaces.
            f.write("%s," % item)
    f.close()

    print("{} has book room #{} at {} to {}.\n".format(
        name, room, starttime, endtime))

#------\------\------GetBookInfo------/------/------#

def GetBookInfo(username):
    with open('MeetingRoom.txt', 'r') as f:                 # This function is meant to retrieve information
        for line in f:                                      # from the text file regarding room number and dates
            if line.startswith(username):                   # based on the user's name
                bookroom = line.split(",")
    return bookroom

#------\------\------\------GetUserBookedRooms------/------/------/------#

def GetUserBookedRooms():
    userinput = input("Please enter your name:\n")          # Name is taken from input.
    bookroom = GetBookInfo(userinput)                       # Bookroom is related to the GetBookInfo function.
    print("{} has book room #{} at {} to {}.\n".format(     # Reads back each part from bookroom as a booking.
        bookroom[0], bookroom[1], bookroom[2], bookroom[3]))

#------\------\------\------DeleteRoom------/------/------/------#

def DeleteRoom():
    import os
    tmp = []
    f = open("MeetingRoom.txt","r")
    for line in f:
        tmp.append(line)
    f.close()
    f = open("MeetingRoom.txt", "w")

    NameI = input("Enter your Booking name:\n")
    for line in tmp:
        if not NameI in line:
            f.write(line)
    f.close()
    print("Your booking is now removed!")
MainMenu()
