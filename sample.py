"""has_laptop = False
has_charger = False

if has_laptop == True and has_charger == True:
    print("Take the assessment")
elif has_laptop == True or has_charger == True:
    print("Take the assessment for now")
else:
    print("Take the assessment tomorrow with minus points")"""

"""# Nested Conditional Statements
# Complex decision making

a = float(input('Enter a number: '))
b = float(input('Enter a number: '))
if a >= 15:
    if b >= 25:
        print("Access Granted")
    elif b < 25:
        print("Access Denied")
else:
    print("Access Denied")"""

"""Math = float(input('Enter a number: '))
Science = float(input('Enter a number: '))

if Math > 85 and Math <= 100:
    if Science >= 90 and Science <= 100:
        print("You are qualified for a special scholarship, congratulations!")
    elif Science > 100:
        print("Please input real scores.")
    else:
        print("You are unqualified as your science score doesn't fit our standards.")
elif Math > 100:
    print("Please input real scores.")
else:
    print("You are not qualified for a special scholarship.")"""

"""a = "~obmc@60th"

if a.isalpha():
    print("All letters detected")
else:
    print("Symbols and numbers detected")"""

#isdigit() - returns true if all the characters are digits, otherwise return false

"""a = '875'

if a.isdigit():
    print("Valid numbers")
else:
    print("Invalid numbers")"""

"""# FUNCTION - any()
# function that returns true if any item in an iterable is TRUE, otherwise False
x = 0
y = 0.555

print(bool(x))
print(bool(y))"""

"""x = []

if any(x):
    print('There is at least 1 non-zero number')
else:
    print("All numbers are zero")"""

"""veggies = ['Carrot', 'Raddish', 'Potato']

for i2 in veggies:
    print("I like", i2 + ".")"""



#Loops - are used to repeatedly execute a block of code until a certain condition is met
# There are 2 main types of loops
#for - lists, tuples, strings, ranges, dictionaries; used for iteration over a sequence.
#i   - iterating var
#in  - kw for checking is something exist inside your seq/data
#var - one that has the data needed

#while - is used to repeatedly execute a block of code as long as a specified condition is TRUE

"""a = True

while a == True:
    print("Hello World")"""

"""age = 12

while age < 21:
    print("verify age:" + str(age))
    age += 1"""

"""numbers = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(numbers):
    if(numbers[i] % 2 == 0):
        print("Even number : " +str(numbers[i]))
        i += 1
    else:
        print("Odd number : " + str(numbers[i]))
        i += 1"""
#continue
"""page = 0
while page < 10:
    page += 1
    if page == 6:
        continue
    print(page)"""

"""for i in range(1,11,2):
#1 - start 11 - stop 2 - step
    print(i)"""
