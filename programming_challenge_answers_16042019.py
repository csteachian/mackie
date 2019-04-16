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
