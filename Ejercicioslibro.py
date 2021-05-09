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

#PRINTING

# type_of_people = 10
# x = f'There are {type_of_people} types of people'

# binary = "binary"
# do_not = "don't"
# y = f"Those who know {binary} and those {do_not}"

# print (y)
# print (x)

# print (f"I said: {x}")
# print (f"I also said: '{y}'")

# hilarius = False
# joke_evaluation = "Isn't that joke so funny?! {}"
# print (joke_evaluation.format (hilarius))

# w = "This is the left sidel of..."
# e = "a string with a right side."
# print (w + e)

#MORE PRINTING

# print ("Mary had a little lamb.")
# print ("Its fleece was white has {}." .format('snow'))
# print ("And everywhere that Mary went.")
# print ("=" * 10) #what'd that do

# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"

#whatch that comma at the end. try removing it to see what happens

# print (end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# print (end7 + end8 + end9 + end10 + end11 + end12)

#PRINTING, PRINTING, PRINTING

# formatter = "{} {} {} {}"

# print (formatter.format (1,2,3,4))
# print (formatter.format ("one", "two", "three", "four"))
# print (formatter.format(True, False, False, True))
# print (formatter.format(formatter, formatter, formatter, formatter))
# print (formatter.format(

# "Si continuas practicando",
# "sin dudas seras",
# "el mejor programando en Pythom.",
# "Sigue practicando"

# ))

# Here's some new strange stuff, remenber type it exactly.

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep"

# print("Here are the days: ", days)
# print ("Here are the months: ", months)

# print ("""
# There's something going on there.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """)

# tabby_cat = "\tI'am tabbed in."
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat."

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
# print (tabby_cat)
# print (persian_cat)
# print (backslash_cat)
# print (fat_cat)

# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()

# print (f"So, you are {age} old, {height} tall and {weight} heavy.")

# print ("Tu edad es:", age, "tu altura es:", height, "tu peso es:", weight)




