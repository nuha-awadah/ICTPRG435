# input validation by using 'while loop + try catch'
while True:
    try:
        #asking the user for their wage
        wagePerMonth = float(input("Enter your wage per hour: "))

        #handles negative number
        if wagePerMonth <= 0:
            print("Please enter a positive number")
        else:
            break
    except ValueError:
        # handles input error
        print("Please enter a numeric value")

#initializing expense category
expenseCategory = input("Enter your expense category: ")
expenseCategory = expenseCategory.upper()

#initializing expense amount
totalExpenseAmount = float(input("Enter your expense amount: "))

#initializing while loop to add more category and amount
continueButton = input("Would you like to continue? (y/n): ")
while continueButton == "y":
    expenseCategory = input("Enter your expense category: ")
    expenseCategory = expenseCategory.upper()
    expenseAmount = float(input("Enter your expense amount: "))
    totalExpenseAmount += expenseAmount

    #repeating the loop
    continueButton = input("Would you like to continue? (y/n): ")

#calculating remaining income after deducting expenses amount
remainingBalance = wagePerMonth - totalExpenseAmount

#display balance
print(f"You have earned ${wagePerMonth} this month. Your total expense is ${totalExpenseAmount}\n"
      f"Your remaining balance is ${remainingBalance}.")

# print(f"\nID : , Initials: ")