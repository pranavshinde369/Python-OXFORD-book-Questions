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

# Q13 Write the program to sum the series 1sq/1 + 2sq/2 + 3sq/3 + 4sq/4 + 5sq/5 + ..+nsq/n

n = int(input("Enter a number: "))
total = 0
for i in range(1, n+1):
    total += (i**2) / i
print(f"Sum of series is: {total}")

# Q14 Write a program that prints a number, its square, and cube repeatedly in the range (1,n).

n = int(input("Enter a number: "))
for i in range (1, n+1):
    print(i,i**2,i**3)

# Q15 Write a program that prompts the user to enter a string. The program calculates and  
# display the length of string until the user enters QUIT (Use While Loop)

while True:
    text = input("Enter a string (type QUIT to exit): ") 
    if text.upper() == "QUIT":
        break
    print(f"length of string:", len(text))

# Q16 Write a program that prompts user to enter numbers. Once the user enters -1, 
# it displays the count, sum, and average of even numbers and that of odd numbers.

count_even = 0
count_odd = 0
sum_even = 0
sum_odd = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))

    if num == -1:
        break

    if num % 2 == 0:
        count_even += 1
        sum_even += num
    else:
        count_odd += 1
        sum_odd += num

avg_even = sum_even / count_even if count_even != 0 else 0
avg_odd = sum_odd / count_odd if count_odd != 0 else 0

print("Even Numbers -> Count:", count_even, "Sum:", sum_even, "Average:", avg_even)
print("Odd Numbers  -> Count:", count_odd, "Sum:", sum_odd, "Average:", avg_odd)\

# Q17 Write a program to calculate electricity bill.

bill = int(input("Enter Consumed unit: "))

if bill <= 150:
    amount = bill * 3
elif bill <= 300:
    amount = (150 * 3) + (bill - 150) * 3.75
elif bill <= 450:
    amount = (150 * 3) + (150 * 3.75) + (bill - 300) * 4
elif bill <= 600:
    amount = (150 * 3) + (150 * 3.75) + (150 * 4) + (bill - 450) * 4.25
else:
    amount = (150 * 3) + (150 * 3.75) + (150 * 4) + (150 * 4.25) + (bill - 600) * 5
print("Your Electricity bill is:", amount)

# Q18 Generate patterns      
# 🔍 Logic: It’s a 5×5 grid,   We print * only on the border,   Inside is empty (spaces)
# 📌 Conditions:   First row → i == 0   Last row → i == 4   First column → j == 0   Last column j == 4
#   *****
#   *   *
#   *   *
#   *   *
#   *****

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Q19 Generate pattern 
#   $ * * * *
#   * $ * * *
#   * * $ * *
#   * * * $ *
#   * * * * $

n = 5
for i in range(n):
    for j in range(n):
        if i == j:
            print("$", end=" ")
        else:
            print("*", end=" ")
    print()


# Q20 A video library rents new video for $75 a day, and old movies for $50 a day. Write a program to
# calculate the total charge for a customer's video rentals. The Program should prompt the user for no of 
# each type of video and outputr the totgal cost

new_videos = int(input("Enter number of new videos: "))
old_movies = int(input("Enter number of old movies: "))

total_cost = (new_videos * 75) + (old_movies * 50)

print("Total cost is ₹", total_cost)