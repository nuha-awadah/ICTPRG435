# varList=[]
# for i in range(5):
# 	varList.append(i-1)             #listVariable.append(value)
# print(varList)

# varList=[]
# for i in range(5):
#     varList.insert(0,i+1)        #listVariable.insert(location, value)
#     print(varList)

# varList = [1,2,3,4,5,6,7]
# del varList[1]
# print(varList)

# varList = [1,2,3,4,5,6,7]
# print(varList[1:4])                 # [2, 3, 4]
# del varList[1:3]                    #[start:stop:step] so will
# print(varList)                      # [1, 4, 5, 6, 7]
# print(varList[1:4])                 # [4, 5, 6]

# Slices have advanced functionality:
# [:] – will show from the start to the finish
# del [:] – will delete all list elements (as it’s the full range).
# [::2] will step through each second element in order.
# [::-2] will step through each second element in reverse order (starting from the last element).

# Useful methods and functions:
# list.append(arg) – As previously mentioned, appends a value onto the end of a list.
# list.insert(i,x) – As previously mentioned, uses an index location (i) and inserts a value (x).
# list.count(x) – gives the amount of occurrences of an element in a list (x).
# list.pop([i]) – removes an element at an indexed position in the list (i). If no value given, removes the last element.
# list.remove(x) – Removes the first instance of a matching element
# list.sort() – Sorts the list in ascending order. We will cover this more next week.
# sorted(list) – This function creates a shallow copy of the list in sorted form, but doesn’t change the original.
# list.reverse() – Reverses the order of the elements in a list.

# varList = [1,2,3,4,5,6,7]
# if 3 in varList:
# 	print("3 is in the list")

# varList = [1,2,3,4,5,6,7]
# sum=0
# for i in varList:
# 	sum += i
# print(sum)

# print('{0:10} {1:10} {2:10}'.format("Number","Squared","Cubed"))      #‘{index:width}’.format(value)
# for x in range(1, 11):
#     print('{0:10} {1:10} {2:10}'.format(x, x*x, x*x*x))


# board=[]
# for i in range(8):
#     row= [ i for i in range(8)]
#     board.append(row)
# print(board,"\n")
#
# rowNum=1
# for i in board:		#This will print it out nicely for us.
#     print("Row", rowNum, i)
#     rowNum += 1

# studentAge= [["Bill",20],["Ryan",16],["Jennifer",28],["Molly",42]]
# # studentAge.sort(key=lambda x: x[1])                    # [['Ryan', 16], ['Bill', 20], ['Jennifer', 28], ['Molly', 42]]
# studentAge.sort(key=lambda x: x[0])         # [['Bill', 20], ['Jennifer', 28], ['Molly', 42], ['Ryan', 16]]
# print(studentAge)

# Sequence - list , tuples, dictionaries
# list - [] square brackets
# tuples - () parenthesis
# dictionaries - {} curly brackets

# Mutability:
# Mutability refers to the term that defines the ability for a type of data to be changed while the program is running.
# Things are either mutable or immutable.
# Objects that are mutable can be changed at any time. This includes appending or deleting a list element.
# Objects that are immutable cannot be modified while the program is running.
# Now, think about a list that could only be created and read. This means you cannot perform the same append or delete functions from before. In fact, if you were to try and append to the list, you would instead have to create a whole new list with the extra element on the end.
# Effectively, it cannot be changed during runtime.
# An example of an immutable data type that we have just described is a Tuple.

# tup1=(1,2,3,4,5)
# tup2=6,7,8,9,10
# tup3=()        # You can create an empty tuple, much in the same form as an empty list.
# print(tup1)
# print(tup2)
# print(tup3)

# tup1=(1,)
# tup2=(2)
# print(tup1)
# print(tup2)

# varTup=(5,10,15,"Green",20.000)
# print(varTup[0])
# print(varTup[-1])
# print(varTup[2:])
# print(varTup[0:3])
# print(varTup[:-2])
# print(varTup[::-1])
# for i in varTup:
# 	print(i)

# Dictionaries are a new mutable and non-sequenced (by default) data type.
# Dictionaries act much in the same way that a physical dictionary does. However, instead think more along the lines of a translation dictionary (e.g. English to Japanese dictionary) than your general dictionary.

# varDictAnimal={’dog’:’inu’, ‘cat’:’neko’, ‘snake’:’hebi’}
# varDictStaffNum={‘Jane’:21646841,’Jack’:84651685,’Bryan’:35254698}
# varDictNothing={}
# print(varDictAnimal)
# print(varDictStaffNum)
# print(varDictNothing)

# lapTimes={}
# while True:
# 	name=input("Enter runners name or press enter to stop: ")
# 	if name == '':
# 		break
# 	time=float(input("Enter runners last time in seconds: "))
# 	if name in lapTimes:
# 		lapTimes[name] += (time,)
# 	else:
# 		lapTimes[name] = (time,)
# for name in sorted(lapTimes.keys()):
# 	sum=0
# 	count=0
# 	for time in lapTimes[name]:
# 		sum +=time
# 		count+=1
# 	print(name, 'has an average lap time of ', sum / count,' seconds.')

# Example 1

# # First, we get the file name from the user.
# file_name = input('Please enter a relative or full text file: ')
#
# # Now we can open the file as read only
# file_object = open(file_name, 'r')
#
# # Print after reading all the contents with the read method.
# print(file_object.read())
#
# # Don't forget to close the file when you are done.
# file_object.close()
#
# # Example 2
#
# # Let’s make a more cat like program that we find in unix based OS's.
#
# # We will need to import the sys module for this to work.
# # https://docs.python.org/3/library/sys.html
# import sys
#
# # Let’s check if the script was run from the console and has at least one
# # argument
# if len(sys.argv) >= 2:
#     file_name = sys.argv[1]  # Index 1 is the first argument after the
#     # script name.
# else:
#     # If there isn't any arguments we can ask for the file name.
#     file_name = input('Please enter a relative or full text file: ')
#
# # If we use the with statement we don't need to run the close method
# # when we are done.
# with open(file_name, 'r') as file_object:
#     print(file_object.read())

# Example 1

# # START
# # READ temp
# temp = float(input('Enter the temperature: '))
# # IF temp < 0
# if temp < 0:
#     # PRINT "Ice"
#     print('Ice')
# # ELSE IF temp > 100
# elif temp > 100:
#     # PRINT "Steam"
#     print('Steam')
# # ELSE
# else:
#     # PRINT "Liquid"
#     print('Liquid')
# # END IF
# # EXIT















