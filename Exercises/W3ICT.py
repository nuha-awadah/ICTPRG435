import math
# print("hello world!")

# string operators
print("hello world!" * 2)

# raw strings - used when you have special characters
# example - you need to display the file path
print(r"C:\Users\Desktop")

# formatted strings
varNum = 9
print(f"the number in var Num is {varNum}")

a="Left"
b="Right"
c="middle"
print(f"{a} and {b} and {c}")

# data types
# = is used when assigning a value ex x = 1
# == is used when checking if something is equal to a value ex 1 == 1

# Network Scripting Lab 2
print("hi user")

userName = input("Enter your name: ")
print(f"Hello {userName}")

numRadius = float(input("Enter a number for a circle radius: "))
areaCircle = (numRadius ** 2) * math.pi
print(f"The area of a circle with radius {numRadius} is {areaCircle}") 