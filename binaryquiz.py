import random

num = random.randint(0,255)
correct = False

while correct != True:
    binary = bin(num)
    print("What is ",binary[2:].zfill(8),"in denary?")
    
    guess = int(input("Your guess "))
    if guess == num:
        correct = True
    else:
        print("Incorrect. Try again.")

print("Well done! You got it right")
