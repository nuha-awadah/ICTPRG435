wagePerHour = float(input(f"What is your wage per hour?\n"))
numberHourWork = float(input(f"How many hours work?\n"))
print(f"You have worked for {numberHourWork} hours and your wage per hour is ${wagePerHour}")

if 40 < numberHourWork <= 168:
    # getting the amount of hours after the first 40 hours
    overtimeHourWork = numberHourWork - 40
    # getting the overtime wage rate
    overtimeWagePerHour = wagePerHour * 1.5
    # calculating the overtime pay
    totalOvertimeWage = overtimeHourWork * overtimeWagePerHour
    print(f"You earned ${totalOvertimeWage} for your overtime")

    # only the first 40 hours has not been calculated
    totalWage = ( 40 * wagePerHour ) + totalOvertimeWage
elif numberHourWork > 168:
    print(f"{numberHourWork} is above the maximum 168 hrs per week.")
    quit()
else:
    totalWage = numberHourWork * wagePerHour

print(f"You earned ${totalWage}")
# print(f"\nID : , Initials: ")

# questions to ask
# 1. i have done the pseudocode and i already have done the code, the next thing to do now is the test plan,
    # when i ran through the test plan, i have not accounted the pseudocode to include where the input is in negative number
    # should i just submit my work with test plan that includes what i should code in to fix the error
    # or
    # i should fix the pseudocode, the code so i dont need to include the explainations in the test plan?
# - the fix is TC-003 and TC-004 to include try catch input validation test, same with scenario 2
# depending on the teacher answer, i should be able to submit this by week 4.
