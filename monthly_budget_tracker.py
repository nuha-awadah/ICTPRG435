# Fixed Pseudocode:
# 1.	BEGIN
# 2.	OUTPUT “Please enter your monthly income”
# 3.	INPUT wagePerMonth
# 4.	WHILE wagePerMonth < 0 OR wagePerMonth == isNumeric
    # a.	OUTPUT “Your wage is in the negatives or is not numeric. Please re-enter your wage”
    # b.	INPUT wagePerMonth
# 5.	ENDWHILE
# 6.	SET totalExpenses = 0
# 7.	OUTPUT “Please enter your expense category and amounts”
# 8.	INPUT expenseCategory
# 9.	INPUT expenseAmount
# 10.	OUTPUT “Do you want to continue (Y/N)?”
# 11.	INPUT continueButton
# 12.	WHILE continueButton = “Y”
    # a.	INPUT expenseCategory
    # b.	totalExpenseCategory = totalExpenseCategory + expenseCategory
    # c.	INPUT expenseAmount
    # d.	totalExpenseAmount =  totalExxpenseAmount + expenseAmount
    # e.	OUTPUT “Do you want to continue (Y/N)?”
    # f.	INPUT continueButton
# 13.	ENDWHILE
# 14.	remainingBalance = wagePerMonth - totalExpenseAmount
# 15.	OUTPUT wagePerMonth,  totalExpenseAmount, remainingBalance
# 16.	END
