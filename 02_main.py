# Q21 Write a program that finds the greatest of three given numbers using functions.
#     pass numbers using arguments

def greater(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num3 and num2 > num1:
        print(num2)
    else:
        print(num3)


greater(20,45,12)


# Q22 Write a program that prints the time taken for execute a program in python

import time

start = time.time()
 # Program code
for i in range(10000):
    pass
end = time.time()

print("time taken for program to execute.",end-start,"seconds")


# Q23 Write a program that uses lambda function to multiply two numbers.

mul = lambda x,y: x*y
print(mul(2,3))

# Q24 Write a program that passes lambda function as an argument to another function
#     to compute the cube of a number.

def calculate(func,num):
    return func(num)

cube = lambda x: x**3


print(calculate(cube,5))

# Q25 Write a function that accepts an integer between 1 and 12 to represent the month number and 
#     displays the corresponding month of the year (for eg month = 1 then display JANUARY)

def month_name(month):
    months = {
        1: "JANUARY",
        2: "FEBRUARY",
        3: "MARCH",
        4: "APRIL",
        5: "MAY",
        6: "JUNE",
        7: "JULY",
        8: "AUGUST",
        9: "SEPTEMBER",
        10: "OCTOBER",
        11: "NOVEMBER",
        12: "DECEMBER"
    }

    if month in months:
        print(months[month])
    else:
        print("Invalid month number")


# Q26 Write a program to concatenate two strings using recursion.

