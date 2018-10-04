# Mr Simpson
import random # loads the module random into python

num = random.randint(0,255) # creates a variable "num" and
                            # setting it to a random number 0 - 255
correct = False # creates a variable "correct" and sets it to False

while correct != True: # compares value of variable "correct"
                       #to NOT True and runs the block of code
                       # until this doesn't match
                       
    binary = bin(num) # creates a variable "binary" and converts number
                       # to a binary sequence
                    
    print("What is ",binary[2:].zfill(8),"in denary?")
    # display binary question
    
    guess = int(input("Your guess ")) # creates a variable "guess" and
                                      # stores the integer number entered
                                      
    if guess == num:  # compares value of variable "guess" to "num"
                       # and IF THE RESULT IS TRUE
        correct = True # changes the variable "correct" to the value True
    else:              # or IF THE RESULT IS FALSE
        print("Incorrect. Try again.") # display error message

print("Well done! You got it right") # display well done message
    













