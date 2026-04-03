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

# Q7 Write a program to input two numbers and check whether they are equal or not.

num1 = int(input("Enter frirst Number: "))
num2 = int(input("Enter second Number: "))
if num1 == num2:
    print("Number is equal")
else:
    print("Number is not equal")


# Q8 Write a program that prompts user to enter a character (O,A,B,C,F).
# Then using if-elif-else construct display Outstanding.

g =str(input("Enter Grade (O, A, B, C, F)"))
grades = g.lower()

if grades=="o":
    print("Outstanding")
elif grades=="a":
    print("very good")
elif grades=="b":
    print("Good")
elif grades=="c":
    print("Average")
elif grades=="f":
    print("Fail")
else:
    print("Enter apporopriate grade")


# Q9 Write a program that determines whether a digit, uppercase, or a lowercase character was entered.

ch = input("Enter a character: ")

if ch.isdigit():
    print("It is a digit")
elif ch.isupper():
    print("It is an uppercase letter")
elif ch.islower():
    print("It is a lowercase letter")
else:
    print("It is a special character")

# Q10 Write a program that count the number of lowercase characters, uppercase characters and digits
# entered by the user

text = input("Enter a sentence")

lower = 0
upper = 0
digit = 0

for ch in text:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    elif ch.isdigit():
        digit += 1

print("lowercase letter", lower)
print("Uppercase letter", upper)
print("Digits", digit)

# Q11 Write a program that displays first 10 natural numbers using loops

for i in range(1, 11):
    print(i)

# Q12 Write a program to find average of first n numberrs using loops.

n = int(input("Enter a number: "))
total = 0 
for i in range(1, n+1):
    total += i
average = total / n
print(f"Average of first {n} numbers is: {average}")

