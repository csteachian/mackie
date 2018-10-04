# Passcode program
letmein = False
while letmein != True:
        username = str(input("enter your username"))
        passcode = str(input("enter your passcode"))
        if passcode == "1234":
                letmein = True
        else:
                print("Password incorrect")
print("Welcome to the system")
