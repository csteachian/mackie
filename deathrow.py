# Mr Simpson
age = int(input("Enter your age")) #declare age as integer

name = str(input("Enter your name")) #declare name as string

food = []
# declare food as list of strings

food.append(str(input("Tell me your first food item")))

food.append(str(input("Tell me your second food item")))

food.append(str(input("Tell me your third food item")))

print("Good evening",name,"this is your menu for tonight.")
# display welcome message to user

for count in range(0,len(food)):
    print(food[count])

print("You are",age,"years old")
















    
