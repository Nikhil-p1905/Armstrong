#-------------------------------------------------------------------------------
# Name:        NIKHIL KUMAR SAH
# Purpose:     Question Solving
#
# Author:      NIKHIL KUMAR SAH
#
# Created:     02-09-2022
# Copyright:   (c) NIKHIL KUMAR SAH 2022
# Licence:     <TROM'S licence>
#------------------------------------------------------------------------------

#Write a program to check if the entered number is Armstrong or not ?

num = int(input("Enter the number as an input value:"))

#initialise sum
sum = 0

#find the sum 0f the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is an Armstrong number")

else:
    print(num,"is not an Armstrong number")

