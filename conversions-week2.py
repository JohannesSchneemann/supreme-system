# Name: Johannes Schneemann
# Date: 1/29/2016
# Description: This is a simple program that uses sequential statements and  
# it will perform the following conversions

# a) miles to kilometer b) Fahrenheit to Celsius c) gallons to liter
# d) pounds to kilograms e) inches to centimeter



# a) get the information (input) for miles to kilometer
# from the user and store it in a variable

number_of_miles = float(input('Johannes, please tell me how many miles do \
you want to convert to kilometers?'))

# perform the conversion in an arithmetic expression

number_of_kilometers = number_of_miles*1.6

# print the result of conversion for the user (output)

print('Johannes,' , number_of_miles ,'miles is equal to', \
      number_of_kilometers,'kilometers!')


# b) get the information (input) for Fahrenheit to Celsius
# from the user and store it in a variable

number_of_fahrenheit = float(input('Johannes, please tell me how \
many degrees Fahrenheit do you want to convert to degrees Celsius?'))

# perform the conversion in an arithmetic expression

number_of_celsius = (number_of_fahrenheit-32)*5/9

# print the result of conversion for the user (output)

print('Johannes', \
      format(number_of_fahrenheit, ',.2f'), \
      'degrees Fahrenheit is equal to', \
      format(number_of_celsius, ',.2f'), \
      'degrees Celsius!')


# c) get the information (input) for gallons to liters
# from the user and store it in a variable

number_of_gallons = float(input('Johannes, please tell me how many \
gallons do you want to convert to liters?'))

# perform the conversion in an arithmetic expression

number_of_liters = number_of_gallons*3.9

# print the result of conversion for the user (output)

print('Johannes,' , number_of_gallons ,'gallons is equal to', \
      number_of_liters,'liters!')


# d) get the information (input) for pounds to kilograms
# from the user and store it in a variable

number_of_pounds = float(input('Johannes, please tell me how many pounds do \
you want to convert to kilograms?'))

# perform the conversion in an arithmetic expression

number_of_kilograms = number_of_pounds*0.45

# print the result of conversion for the user (output)

print('Johannes,' , number_of_pounds ,'pounds is equal to', \
      number_of_kilograms,'kilograms!')

# e) get the information (input) for inches to centimeter
# from the user and store it in a variable

number_of_inches = float(input('Johannes, please tell me how many inches do \
you want to convert to centimeters?'))

# perform the conversion in an arithmetic expression

number_of_centimeters = number_of_inches*2.54

# print the result of conversion for the user (output)

print('Johannes,' , number_of_inches ,'inches is equal to', \
      number_of_centimeters,'centimeters!')





                                   








