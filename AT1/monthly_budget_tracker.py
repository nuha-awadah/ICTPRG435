# input validation while loop + try catch
while True:
    try:
        wagePerMonth = float(input("Enter your wage per hour: "))
        if wagePerMonth <= 0:
            print("Please enter a positive number")
        else:
            break
    except ValueError:
        # handles input error
        print("Please enter a numeric value")

expenseCategory = input("Enter your expense category: ")
expenseCategory = expenseCategory.upper()
totalExpenseAmount = float(input("Enter your expense amount: "))

continueButton = input("Would you like to continue? (y/n): ")

while continueButton == "y":
    expenseCategory = input("Enter your expense category: ")
    expenseCategory = expenseCategory.upper()

    expenseAmount = float(input("Enter your expense amount: "))
    totalExpenseAmount = totalExpenseAmount + expenseAmount

    continueButton = input("Would you like to continue? (y/n): ")

remainingBalance = wagePerMonth - totalExpenseAmount
print(f"You have earned ${wagePerMonth} this month. Your total expense is ${totalExpenseAmount}\n"
      f"Your remaining balance is ${remainingBalance}.")

# print(f"{expenseCategory} expense is ${totalExpenseAmount}")
# print(f"\nID : , Initials: ")