"""The question is: How many coins does it take to fill a room?
We need to know: 

    How big is the room?

    Is it a specific coin or are there a mix?
    How big are the coins?  Each one.

"""

# get the size of the room in the metric system (meters, centimeters, etc...)
room_size = input('Do you know the size of the room in the metric system? (y)es | (n)o :')

if room_size == 'y' or room_size == 'Y' or room_size == 'Yes' or room_size == 'yes':
    room_size = input('What is the size of the room?')
else:
    width = float(input('What is the width of the room?'))
    length = float(input('What is the length of the room?'))
    height = float(input('what is the height of the room?'))
    room_size = width*length*height

# print(room_size + 'cubic meter(m**3)')

# establish size of coins in cubic meters
quarter = float(.000000808)
dime = float(.00000034)
nickel = float(.000000688)
penny = float(.000000442)
x = quarter + dime + nickel + penny
average = x/4 

# divide room size by coin size
total_quarters = round(float(room_size)/quarter)
total_dimes = round(float(room_size)/dime)
total_nickels = round(float(room_size)/nickel)
total_pennies = round(float(room_size)/penny)
total_average = round(float(room_size)/average)


print(f'{total_quarters} quaters\nor\n{total_dimes} dimes\nor\n{total_nickels} nickels\nor\n{total_pennies} pennies\nor\n{total_average} mixed')