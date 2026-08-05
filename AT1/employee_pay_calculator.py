# PseudoCode
# BEING
# INPUT wagePerHour
# INPUT numberHourWork
# IF numberHourWork > 40 AND numberHourWork ≤ 168
#     overtimeHourWork = numberHourWork – 40
#     overtimeWagePerHour = wagePerHour * 1.5
#     totalOvertimeWage = overtimeHourWork * overtimeWagePerHour
#     totalWage = ( numberHourWork * wagePerHour ) + totalOvertimeWage
# ELSE IF numberHourWork > 168
#     OUTPUT “Number of hours work in a week is 168. Please reenter”
# ELSE
#     totalWage = numberHourWork * wagePerHour
# OUTPUT totalWage
# END

wagePerHour = float(input(f"What is your wage per hour?\n"))
numberHourWork = float(input(f"How many hours work?\n"))
print(f"You have worked for {numberHourWork} hours and your wage per hour is ${wagePerHour}")

if 40 < numberHourWork <= 168:
    overtimeHourWork = numberHourWork - 40
    overtimeWagePerHour = wagePerHour * 1.5
    totalOvertimeWage = overtimeHourWork * overtimeWagePerHour
    print(f"You earned ${totalOvertimeWage} for your overtime")
    totalWage = ( numberHourWork * wagePerHour ) + totalOvertimeWage
elif numberHourWork > 168:
    print(f"{numberHourWork} is above the maximum 168 hrs per week. Please try again.")
    quit()
else:
    totalWage = numberHourWork * wagePerHour

print(f"You earned ${totalWage}")