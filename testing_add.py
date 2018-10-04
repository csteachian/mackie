# I Simpson
# Ask for two numbers and add them together
def check(min,max):
    validnum = int(input("Enter a number"))
    while (validnum < min) or (validnum > max):
        print("Error. Needs to be between",min,"and",max)
        validnum = int(input("Enter a number"))    
    # if program gets here min<validnum<max
    return validnum

number1 = check(-10,10)
number2 = check(100,200)
answer = number1 + number2
print("The total is ",answer)
            
