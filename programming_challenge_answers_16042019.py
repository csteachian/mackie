# Programming challenge 1

# The program asks the user for a car make,
# model and daily rate 1 then displays a table
# of daily charges for between one and fourteen days.
make = input("Enter make")
model = input("Enter model")
dailyrate = int(input("Enter daily rate"))

print("Day","Charge")
for day in range(1,15):
    print(day,(dailyrate*day))

if (make.lower() == "fiat"):
    print("You have a free atlas")

# Programming challenge 2

# You are required to write a program to count the
# number of pupils in a class of twelve who score over
# 40 in a test out of 60.  The pupils’ marks are to be
# entered at the keyboard.  The output is a message that
# indicates the number of pupils who score more than 40.

#
numberofpupils = 12
maxscore = 60
minscore = 0
threshold = 40
counttotal = 0

for index in range(1,numberofpupils+1):
    mark = int(input("Enter mark for pupil: "))
    # input validation
    while (mark < minscore) or (mark > maxscore):
        print("Error")
        mark = int(input("Enter mark for pupil: "))

    if (mark > threshold):
        counttotal += 1

print("Number of pupils who scored >40: ",counttotal)

# Programming challenge 3

# A group of twelve office workers decides to have a
# weekly charity lottery.  Each worker is asked to
# contribute €1 and a draw is made.  The winner gets half
# of the contributions with the other half going to
# charity.  If the person selected has not paid that
# week, all contributions go to charity.  You are
# required to write a program that selects a winner
# from a set of workers’ names read from data statements
# and held in an array.  The user is asked if the
# selected person has paid that week.  The input should
# be validated.  An appropriate message is given.
import random

workers = ["Jackson","Alistair","Adam","Joe","John","Connor","Ross",
           "Ciaran","Iona","Amy","Aiden","Jodie"]
cost_each = 1.00
number_of_workers = 12
worker_drawn = random.randint(0,number_of_workers-1)

print("Draw has been made")
print(workers[worker_drawn],"is the winner!")
has_paid = input("Has this person paid this week?")
while has_paid.upper() != "Y" and has_paid.upper() != "N":
    print("Error. Must be Y or N.")
    has_paid = input("Has this person paid this week?")
    
if has_paid.upper() == "Y":
    print(workers[worker_drawn],"has won £",str(float((number_of_workers*cost_each)/2)))
    print("The same amount is donated to charity.")
else:
    print("All the money is donated to charity. They receive £",str(float(number_of_workers*cost_each)))
