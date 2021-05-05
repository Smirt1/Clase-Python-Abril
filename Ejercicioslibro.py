#PRINT

# print ("Hello Work!")
# print ("Hello Again")
# print ("I like typing this.")
# print ("This is fun.")
# print ('Yay! Printing')
# print ("I'd much rather you 'not'.")
# print ('I "said do not touch this."')

#COMMENT

#A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

#print ("I could have code like this.") # and the comment after is ignored

#Yo can also use a comment to 'disable' or comment out code:
#print ("This won't run")
#print ("This will run. ")

#NUMBERS AND MATH

# print ("I will now count my chikens: ")

# print ("Hens", 25 + 30 / 6) #suma, division
# print ("Roosters", 100 - 25 * 3 % 4) # resta, multiplicacion, residuo

# print ("Now I will count the eggs:")

# print (3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6) #suma, resta, residuo, division decimal

# print ("Is it true that 3 + 2 < 5 - 7?") #suma, comparacion, resta

# print (3 + 2 < 5 - 7) 

# print ("What is 3 + 2?", 3 + 2)
# print ("What is 5 - 7?", 5 - 7)

# print ("Oh, that's why it's False.")

# print ("How about some more")

# print ("Is it greater?", 5 > -2)
# print ("Is it greater or equal?", 5 >= -2)
# print ("Is it less or equal?", 5<= -2)

#VARIABLES

# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven

# print ("There are", cars, "cars available.")
# print ("There are only", drivers, "drivers available.")
# print ("There will be", cars_not_driven, "empty cars today.")
# print ("We can transport", carpool_capacity, "people today." )
# print ("We have", passengers, "to carpool today.")
# print ("We need to put about", average_passengers_per_car, "in each car.")

# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print (f"Let's talk about {my_name}.")
# print (f"He's {my_height} inches tall.")
# print (f"He's {my_weight} pound heavy.")
# print ("Actually that's not too heavy")
# print (f"He;s got {my_eyes} eyes and {my_hair} hair.")
# print (f"His teeth are usually {my_teeth} depending on the coffee.")

# total = my_age + my_height + my_weight #tricky line
# print (f"If I add {my_age},{my_height}, and {my_weight} I get {total}.")

# name = 'Zed A. Shaw'
# age = 35 # not a lie
# height = 74 # inches
# weight = 180 # lbs
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'

# conv_ak = weight * 0.45 #convirtiendo libras a kilos
# conv_ac = height * 2.54 #convirtiendo pulgadas a centimetos

# print ("Mi nombre es:", name)
# print ("Tengo", conv_ak, "kilogramos")
# print ("Mido", conv_ac, "centimemtros")

type_of_people = 10
x = f'There are {type_of_people} types of people'

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those {do_not}"

print (y)
print (x)

print (f"I said: {x}")
print (f"I also said: '{y}'")

hilarius = False
joke_evaluation = "Isn't that joke so funny?! {}"
print (joke_evaluation.format (hilarius))

w = "This is the left sidel of..."
e = "a string with a right side."
print (w + e)