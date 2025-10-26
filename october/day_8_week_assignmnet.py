'''Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen
'''

num1 = int(input("provide me your first num: "))
num2 = int(input("provide me your second num: "))

sum = (num1 + num2)
print("Addition: ",sum)

sub = (num1 - num2)
print("Subtraction: ",sub)

Multi = (num1 * num2)
print("Multiplication: ",Multi)

div = (num1 / num2)
print("Division: ",div)

'''Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your second name: ")

full_name = (first_name + " " + last_name)

print("Welcome MR:",full_name)