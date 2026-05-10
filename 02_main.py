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

monthno = int(input("Enter month number"))
month_name(monthno)

# Q26 Write a function that accepts a number n as input and returns 
#     the average of numbers from 1 to n 

def num_avg(n):
    num=0
    for i in range(0,n+1):
        num += i
    return num/n

numm = int(input("enter a number"))
print(num_avg(numm))

# Q27 Write a program to calculate te area of triangle using a function

def traiangle_area(base,height):
    return 1/2 * base * height

print(traiangle_area(3,4))

# Q28 Write a program using function that returns the surface area and volume of a sphere.

def sphere(radius):
    surface_area = 4 * 3.141 * radius**2
    volume_sphere = 4/3 * 3.141 * radius**3
    print("Surface area of sphere =",surface_area)
    print("Volume of sphere =",volume_sphere)

sphere(5)


# Q29 Write a Program to reverse a string without recursion

string = input("enter a string:")

reverse_string = string[::-1]
print("reversed string:", reverse_string)

# Q30 Write a function to print a table of binomial coefficients B(m,x) = m! / (x!(m-x)!) where m>x

def factorial(n):  #function to calculate factorial
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def binomial(m, x):
    
    return factorial(m) // (factorial(x) * factorial(m - x))

n = int(input("Enter number of rows: "))  # Printing table of binomial coefficients

for m in range(n + 1):
    for x in range(m + 1):
        print(binomial(m, x), end=" ")
    print()