## Intermediate Expressions (Order of Operators)
## Parenthesis
## Power
## Multiplication/Division
## Addition/Subtraction
## Left to right

## exercise

# width = 15
# height = 12
# print(height/3)


## range and pass function

# for i in range(1,5,2):
#     pass
# print(i)


## Comparison Operators

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


## Excercise 02 - 02

# nzt = ('Enter your name: ')
# print("Hello",nzt)

## Excerside 02 - 03

# xh = input("Enter Hours: ")
# xr = input("Enter Rate: ")
# xp = float(xh) * float(xr)
# print("Pay",xp)


# perfection = input("Hours a Day: ")
# grinder = input("Days a Week: ")
# master_of_craft = float(perfection) * float(grinder)
# print("10,000's to Master my Craft", master_of_craft)

## try / except

## Example 1

# astr = 'Bob'
# try:
#     print('Hello')
#     istr = int(astr)
#     print('There')
# except:
#     istr = -1

# print('Done', istr)

## Example 2

# rawstr = input('Enter a number:')
# try:
#     ival = int(rawstr)
# except:
#     ival = -1

# if ival > 0 :
#     print('Nice work')
# else:
#     print('Not a number')

## 03 - 02

## Code of hrs plus ot (it will error if you spell out ten though (str))

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

## try accept fix for spelling error

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

## Python Function A Built in

# big = max('Hello world')
# print(big) # Finds the w

# tiny = min('Hello world')
# print(tiny) # Finds the   (space)

## Creating a function (call and return)

# x = 5
# print('Hello')

# def print_lyrics():
#     print("I'm a lumberjack, and I'm Okay.")
#     print('I sleep all night and I work all day.')

# print('Yo')
# print_lyrics()
# x = x + 2
# print(x)

## Function parameters

# def greet(lang):
#     if lang == 'es':
#         print('Hola')
#     elif lang == 'fr':
#         print('Bonjour')
#     else:
#         print('Hello')

# greet('en')
# greet('es')
# greet('fr')

## Functions return values

# def greet():
#     return "Hello"

# print(greet(), "Glenn")
# print(greet(), "Sally")

## Fruitful function returning results or return value

# def greet(lang):
#     if lang == 'es':
#         return 'Hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'

# print(greet('en'), 'Glenn')
# print(greet('es'),'Sally')
# print(greet('fr'),'Michael')

## While loop repeated steps 5,4,3,2,1

# n = 5
# while n > 0 :
#     print(n)
#     n = n - 1
# print('Blastoff!')
# print(n)

## Infinite Loop (Don't use)

# n = 5
# while n> 0 :
#     print('Lather')
#     print('Rinse')
# print('Dry off!')

## Break in a loop (need to type in the terminal)

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done')

## Finish iteration with continue (type in the therminal)
# while True:
#     line = input('> ')
#     if line[0] == '#' :
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

## Simple definite loop

# for i in [5, 4, 3, 2, 1] :
#     print(i)
# print('Blastoff')

## Definite loop with strings

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print('Happy New Year:', friend)
# print('Done!')

## Loop idioms

# Example 1
# print('Before')
# for thing in [9, 41, 12, 3, 74, 15] :
#     print(thing)
# print('After')

# Example 2

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15] :
#     if the_num > largest_so_far :
#         largest_so_far = the_num
#     print(largest_so_far, the_num)

# print('After', largest_so_far)

