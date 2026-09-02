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
# First we will start with an empty list that we can add to.
my_list = []

# We will then create a loop that will ask for 5 inputs and work out the
# minimum and the maximum each time.

for i in range(5):
    new_num = int(input("Please enter an integer: "))
    # We need to add this value into the list.
    my_list.append(new_num)
    # To demonstrate the list each cycle, let's show it at each step.
    print("The current list is:", my_list)
    print("The current minimum number is", min(my_list))
    print("The current maximum numbers is", max(my_list),
          # We'll add a new line to make things more presentable each
          # cycle
          "\n")

# Example 2
# We will use the same list from above, but this time use a while loop
# and let the user break out when ready

while True:
    # We can't type cast the input because the user may be inputting a
    # string OR an integer
    new_num = input("Please enter an integer, or type q to finish: ")

    # We check the first index point of the input (once converted to
    # lowercase) to see if it starts with a 'q'.
    if new_num.lower()[0] == "q":
        # If it does we want to break out of the loop and end the
        # program.
        break
    else:
        # We need to add this value into the list.
        my_list.append(int(new_num))
        # To demonstrate the list each cycle, let's show it at each
        # step.
        print("The current list is:", my_list)
        print("The current minimum number is", min(my_list))
        print("The current maximum numbers is", max(my_list),
              "\n")