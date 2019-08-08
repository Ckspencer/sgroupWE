def MainMenu():
    print("Please select an option:")
    print("[0] Exit Program")
    print("[1] Add Booking")
    print("[2] Edit Booking")
    print("[3] Check Availbility")
    userinput = int(input("Please select an option:"))    

    #Check for int input
    if (isinstance(userinput, int)):
        pass
        
    #Check if int is in range
    if (userinput <= 0 or userinput >= 3):
        pass
        
    #Direct via user input
    if (userinput == 0):
        exit()
    elif (userinput == 1):
        BookRoom()
    elif (userinput == 2):
        pass
    else (userinput == 3):    
        pass

def BookRoom():
    Name = input("Please enter your name: ")
    Room = input("Select a Room [1-4]: ")
    SDate = input("Input a date when the meeting will start, with the format of [D/M/YEAR]: ")      #Start Date is inputed from user.
    EDate = input("Input a date when the meeting will End, with the format of [D/M/YEAR]: ")        #End Date is inputed from user.
    STime = input("Select a time when the meeting will start, with the format of [Hr:Min]: ")       #Start Time is inputed from user.
    ETime = input("Select a time when the metting will End,with the format of [Hr:Min]: ")          #End Time is inputed from user.

    Booking = [Name, Room, SDate, EDate, STime, ETime]

#Prints out a welcome message to user.
print("Welcome to the meeting room booking system!")          	
print(" ")
MainMenu()
    
