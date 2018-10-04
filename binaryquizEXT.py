import random

num = random.randint(0,255)
correct = False

attempts = 0

while (correct != True) and (attempts < 3):
    
    attempt = attempt + 1
    
    binary = bin(num)
    print("What is ",binary[2:].zfill(8),"in denary?")
    
    guess = int(input("Your guess "))
    if guess == num:
        correct = True
    else:
        print("Incorrect. Try again.")

if (attempts >= 3):
    print("The right answer was",num)
    print("Try again soon!")
else:
    print("Well done! You got it right")






    
