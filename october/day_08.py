# print ()functions

name = "john"
age = 20

print("Name:",name, "Age:",age)

day = 10
month = 3
year = 2020

print(day,month,year,sep = "/")

# Input ()functions

name = input("provide me your name: ")
age = int(input("rovide me your age:")) # (all input value is str so we have to convert its data type)
print("your name is: ",name, "and your age is: ",age)

# Coding exercise

# Find out area of triangle

a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of triangle is ", round(area,2))

'''
Simple Interest = (P * R * T)/100
P = Principal amount
R = Rate of interest
T = Time duration
'''

principal = float(input("Enter principal amount: "))
rate = float(input("Enter intrest rate : "))
time = float(input("Enter time period: "))

s1 = (principal * rate * time)/100
print("Simple interest is: ",s1)