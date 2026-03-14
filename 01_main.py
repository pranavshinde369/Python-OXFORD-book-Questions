# Q1 Write Python Program to enter two integer and then perform all arithmetic operation on them.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
add = a + b 
sub = a - b
mul = a * b
div = a / b
print(add,sub,mul,div)

# Q2 Write a prograam to perform string concatentation.

str1 = "Hello"
str2 = "World"

result = str1 + " " + str2
print(result)
 

name = "Pranav"
age = 19

result = f"My name is {name} and I am {age} years old."
print(result)


# Q3 Write a program to print the ASCII values of a character.

'''   
ASCII stands for American Standard Code for Information Interchange.
ASCII values are numeric codes assigned to characters (letters, digits, symbols)
so computers can store and process text.
'''

char = str(input("Enter singler character to see its ASCII value"))
ASCIIno = ord(char)
print(f"ASCII no of {char} is {ASCIIno} ")

# Q4 Write a program to to swap two numbers using temporary variable.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

c = a 
a = b 
b = c 

print("After swapping:")
print("First number =", a)
print("Second number =", b)

# Q5 Write simple program to calculate simple intrest and compound intrest.

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest (%): "))
t = float(input("Enter Time (in years): "))

si = (p * r * t) / 100

amount = p * (1 + r/100) ** t
ci = amount - p

print("Simple Interest =", si)
print("Compound Interest =", ci)

# Q6 Write a program that calculates no of seconds in a day.

day = 24 #h 
one_hour = 60 #min
one_min = 60 #sec

sec_in_day = day*one_hour*one_min
print(f"seconds in a day:{sec_in_day}")