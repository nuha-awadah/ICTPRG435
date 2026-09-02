# There are two important rules with using functions!
# You cannot call a function which isn’t already known at the runtime of its call
#
# text()
#
# def text():
# 	print(“Enter an integer amount”)
#
# print(“Starting”)
# varA= int(input())

# You can’t have a function and a variable use the same name.
# To an extent this still runs, BUT, text now only holds the value of the input, it has completely forgotten about our function.

# def text():
# 	print("Enter an integer amount")
#
# print("Starting")
# text= int(input())

# def text(number):
# 	print("Enter an integer amount")
#
# text()

# This is what we call shadowing. You can have an external variable and a parameter exist with the same name.
# A parameter shadows the variable with the same name, BUT, only inside of the function.
# Parameter number and variable number are two wholly different objects to python.

# def text(number):
# 	print("Enter an integer amount", number)
#
# number=999
# text(7)
# print(number)

# def text(item,number):
# 	print("Enter an item: ", item, "\nEnter an integer amount: ", number)
#
# text("Milk")
# TypeError: text() missing 1 required positional argument: 'number

# def text(item,number):
# 	print("Enter an item: ", item, "\nEnter an integer amount: ", number)
#
# text(7, "Milk")
# text(1, "Bread")
#
# def text(item,number):
# 	print(“Enter an item: ”, number, “\nEnter an integer amount: ”, item)
#
# text(7, “Milk”)
# text(1, “Bread”)






# Write Python code for a loop that simultaneously computes both the maximum and minimum of a list.
# Example 1
# # First we will start with an empty list that we can add to.
# my_list = []
#
# # We will then create a loop that will ask for 5 inputs and work out the
# # minimum and the maximum each time.
#
# for i in range(5):
#     new_num = int(input("Please enter an integer: "))
#     # We need to add this value into the list.
#     my_list.append(new_num)
#     # To demonstrate the list each cycle, let's show it at each step.
#     print("The current list is:", my_list)
#     print("The current minimum number is", min(my_list))
#     print("The current maximum numbers is", max(my_list),
#           # We'll add a new line to make things more presentable each
#           # cycle
#           "\n")
#
# # Example 2
# # We will use the same list from above, but this time use a while loop
# # and let the user break out when ready
#
# while True:
#     # We can't type cast the input because the user may be inputting a
#     # string OR an integer
#     new_num = input("Please enter an integer, or type q to finish: ")
#
#     # We check the first index point of the input (once converted to
#     # lowercase) to see if it starts with a 'q'.
#     if new_num.lower()[0] == "q":
#         # If it does we want to break out of the loop and end the
#         # program.
#         break
#     else:
#         # We need to add this value into the list.
#         my_list.append(int(new_num))
#         # To demonstrate the list each cycle, let's show it at each
#         # step.
#         print("The current list is:", my_list)
#         print("The current minimum number is", min(my_list))
#         print("The current maximum numbers is", max(my_list),
#               "\n")

# Write Python code which sorts a list of string by increasing length.
# Again we start with a pre-defined list (if you want, you could as
# the user for inputs to sort instead).

# word_list = [
#     "This",
#     "will",
#     "be",
#     "all",
#     "jumbled",
#     "up",
#     "at",
#     "the",
#     "end"]
#
# # Let's print it out as is first off.
# print(word_list)
#
# # We then need to sort the list, based on the length of the characters.
# word_list.sort(key=len)
#
# # Then we will print out the sorted list.
# print(word_list)


# Write a program that sorts a 2D list of Country objects in decreasing order so that the most populous country is at the beginning of the list.
# We will need a list that has an element containing both the country
# and its population as a singular element, as such we will use 2D
# lists. We'll use the one further on in the lab.

# country_list = [["Africa", 1766], ["Asia", 5268], ["Australia", 46], [
#     "Europe", 628], ["North America", 392], ["South America", 809]]

# This one is tricky, because something that we will learn about next, Dictionaries, will make life a lot easier.
# We can use the lambda mini function to sort by the second sub-element in each main element.
# We can also use the reverse argument to sort in descending order.

# country_list.sort(key=lambda x: x[1], reverse=True)
# print(country_list, "\n")

# Let's print it out in a nicer format using the format function. Think of it as a prototype for our table.

# print("{0:15} | {1:20}".format("Country", "Population in millions"))
# for i in country_list:
#     print("{0:15} | {1:20}".format(i[0], i[1]))



# Write a loop that fills a list values with ten random numbers between 1 and 100.
# The easiest way to include randomised numbers, ranges, and choices is the random module, so we need
# to import it as it is not built in to Python.

import random

# We need to start off with an empty list we will later fill with random values.
rand_list = []

# We now need to have a loop that will run 10 times and append a random number each time.

for i in range(10):
    # We will use the list append method and use the randrange method of the random module.
    rand_list.append(random.randrange(0, 100))
print(rand_list)




# Write a program that reads in a text file, converts all words to lowercase, and prints out all words in the file
# that contain the letter a, the letter b, and so on. Build a dictionary whose keys are the lowercase letters, and
# whose values are sets of words containing the given letter.

# Logic
