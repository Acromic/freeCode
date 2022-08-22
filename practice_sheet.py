# Intermediate Expressions (Order of Operators)
# Parenthesis
# Power
# Multiplication/Division
# Addition/Subtraction
# Left to right

# exercise
# width = 15
# height = 12
# print(height/3)


# range and pass function
# for i in range(1,5,2):
#     pass
# print(i)


# Comparison Operators

# x = 5

# if x == 5:                                # Equals 5
#     print('Equals 5')
# if x > 4:                                 # Greater Than 4
#     print('Greater than 4')
# if x >= 5:                                # Greater than or Equals 5
#     print('Greater than or Equals 5')
# if x < 6:                                 # Less than 6
#     print('Less than 6')
# if x <=5:                                 # Less than or Equals 5
#     print('Less than or Equals 5')
# if x != 6:                                # Not equal 6
#     print('Not equal 6')


# Excercise 02 - 02

# nzt = ('Enter your name: ')
# print("Hello",nzt)

# Excerside 02 - 03

# xh = input("Enter Hours: ")
# xr = input("Enter Rate: ")
# xp = float(xh) * float(xr)
# print("Pay",xp)


# perfection = input("Hours a Day: ")
# grinder = input("Days a Week: ")
# master_of_craft = float(perfection) * float(grinder)
# print("10,000's to Master my Craft", master_of_craft)

# try / except

# Example 1

# astr = 'Bob'
# try:
#     print('Hello')
#     istr = int(astr)
#     print('There')
# except:
#     istr = -1

# print('Done', istr)

# Example 2

# rawstr = input('Enter a number:')
# try:
#     ival = int(rawstr)
# except:
#     ival = -1

# if ival > 0 :
#     print('Nice work')
# else:
#     print('Not a number')

# 03 - 02

# Code of hrs plus ot (it will error if you spell out ten though (str))

# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# fh = float(sh)
# fr = float(sr)

# if fh > 40 :
#     reg = fr * fh
#     otp = (fh - 40) * (fr * 0.5)
#     xp = reg + otp
# else:
#     xp = fh * fr
# print("Pay:",xp)

# try accept fix for spelling error

# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# try:
#     fh = float(sh)
#     fr = float(sr)
# except:
#     print("Error, please enter numeric input")
#     quit() # quit stopped from throwing an error in the try and except block

# print(fh, fr)
# if fh > 40 :
#     reg = fr * fh
#     otp = (fh - 40) * (fr * 0.5)
#     xp = reg + otp
# else:
#     xp = fh * fr
# print("Pay:",xp)

# Python Function

big = max('Hello world')
print(big) # Finds the w

tiny = min('Hello world')
print(tiny) # Finds the   (space)