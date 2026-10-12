# return
# With just the keyword, it will cause the function to finish immediately in place, returning to the point it was
# called without further running the rest of the function. This automatically happens at the end of the function
# (this is essentially the same as break in a loop

# def number():
# 	print("1")      # Part of the function code
# 	return 2        # Returns from function, with 2 as the result
# 	print("3")      # Doesn’t run
#
# print("And the number is.....")
# print(number())

# def funkyFunction():
# 	print(“Is it funky?”)
#
# varA=funkyFunction()
#
# if varA == None:
# 	print(“It’s not very funky…”)
# else:
# 	print(“That’s pretty funky!”)
#

# def ifEven(n):
#     if (n % 2 == 0):
#         return True
#
# varNum=int(input(“Enter a number, is it truly even? ”))
# print(“For”, varNum, “it is :”, ifEven(varNum))
#
# Arguments: Live outside the associated function and feed information into the functions.
# Parameters: Only live inside a function and need to be stated inside the brackets of the def statement.

# def num():
# 	varNum=20  #varNum is out of your scope : A scope of something in Python is the areas in which it will be recognised.
# num()
# print(varNum)

# def num():
# 	print("Do I know the number?", varNum)
#
# varNum=20
# num()
# print(varNum)

# def num():
# 	global varNum
# 	varNum=10
# 	print("Do I know the number?", varNum)
#
# varNum=20
# num()
# print(varNum)

# def num(n):
# 	print("It is: ", n)
# 	n+=1
# 	print("Now it is: ", n)
#
# varNum=20
# num(varNum)
# print(varNum)
#
#
# def num(fList):
#     print(fList)
#     fList = [7, 8, 9]
#
#
# L = [4, 5, 6]
# num(L)
# print(L)


# def functionName(parameter):
#     functionBody

# def fib(n):     #Call the function
# 	if n < 1:
# 		return 0
# 	if n < 3:
# 		return 1                #Handles numbers 0-2
# 	num1 = num2 = 1             #Assign beginning variable values
# 	sum = 0
# 	for i in range(3, n+1):     #Loop through the process from 3 onwards to get the final sum value.
# 		sum = num1 + num2       #Assigning sum and then shifting the num values “up” a space
# 		num1, num2 = num2, sum
# 	return sum                  #Return the end result
#
# for i in range(10):
# 	print("Fibonacci " + str(i), "=", fib(i))

# Recursion is the concept within programming that relates to an instance of a function invoking itself.

# def fib(n):
# 	if n < 1:
# 		return 0
# 	if n < 3:
# 		return 1
# 	return fib(n-1) + fib(n-2)			#This is where the algorithm is
#
# for i in range(10):
# 	print("Fib" + str(i), "=", fib(i))
#
# def fib(n):
# 	if n < 1:
# 		return 0
# 	if n < 3:
# 		return 1
# 	print(“calculating: ”, fib(n-1),fib(n-2))
# 	return fib(n-1) + fib(n-2)
#
# for i in range(6):
# 	print(“Fib” + str(i), “=“, fib(i))

# def lessThanTen(n):
#     if n < 10:
#         print(n)
#         return lessThanTen(n+1)
#     return n
#
# varNum = float(input('Enter a number less than 10 and we’ll count the rest for you: '))
# print(lessThanTen(varNum))

a = 0
b = 5

def main():
	global a,b
	i = 10			# 
	b = g(i)		# global b,
	print(a+b+i)

def f(i):
	n = 0
	while n * n <= i :
		n = n + 1
	return n - 1

def g(a):
	b = 0
	for n in range(a):
		i = f(n)
		b = b + i




