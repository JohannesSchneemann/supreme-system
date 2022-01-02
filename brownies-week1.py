# Name: Johannes Schneemann
# Date: 1/2/2022
# Description:  Program that describes how many brownies will fit
#               in a baking pan of a specified size

# Declare all needed variables. Give each variable a descriptive name
# write statements to prompt the user for input
# perform necessary calculations to get desired output

# get the information (input) for the brownies from the user
width_brownie = float(input('What is the width of your brownie?'))
length_brownie = float(input('What is the length of your brownie? '))
number_brownie = float(input('How many brownies do you have? '))
print("\n")

# calculate the area of the brownie
area_brownie = width_brownie*length_brownie

# get the input from the user for the baking pan
width_baking_pan = float(input('What is the width of your baking pan? '))
length_baking_pan = float(input('What is the length of your baking pan? '))
print("\n")

# calculate the area of the baking pan
area_baking_pan = width_baking_pan*length_baking_pan

# calculate number of brownies
number_of_brownies = area_baking_pan / area_brownie

# answer
print("Your baking pan can hold", '%4.2f' % number_of_brownies, 'brownies.')
