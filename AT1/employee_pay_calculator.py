# asking the user for their wage inputs

#included try catch block to fix
while True:
    try:
        wagePerHour = float(input("What is your wage per hour?\n"))
        if wagePerHour < 0:
            print("Invalid input. Wage cannot be negative. Please try again.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.\n")

while True:
    try:
        numberHourWork = float(input("How many hours work?\n"))
        if numberHourWork < 0:
            print("Invalid input. Hours cannot be negative. Please try again.\n")
            continue
        if numberHourWork > 168:
            print("Invalid input. Hours cannot exceed 168 per week. Please try again.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numerical value.\n")

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

# else if when the number of hours works exceeds 168
elif numberHourWork > 168:
    print(f"{numberHourWork} is above the maximum 168 hrs per week.")
    quit()

# else when the number of hours work is under 40
else:
    totalWage = numberHourWork * wagePerHour

print(f"You earned ${totalWage}")
print(f"\nID :, Initials: ")

