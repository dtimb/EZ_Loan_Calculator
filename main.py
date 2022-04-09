"""
E-Z Loan Calculator
Dylan Timbrook
4/9/2022
Display loan payment / payment plan based on a user-given principal, APR, and term.
Calculates monthly payment, total interest, and total cost on a separate 'loan_calc' file.
"""

import loan_calc # calculations imported from file 'loan_calc'

# user input
amount = float(input("Enter the amount of the loan:\n"))
apr = float(input("Enter the annual percentage rate (APR):\n"))
num_months = int(input("Enter the number of months for the loan:\n"))

count = 1

# calculates payment, interest, and the total cost using functions from 'loan_calc'
MP = float(loan_calc.calculate_payment(amount,apr,num_months))
TI = float(loan_calc.total_interest_paid(amount,apr,num_months))
TC = float(loan_calc.total_loan_cost(amount,apr,num_months))

new_payment = 0
new_principal = 0
new_intrest = 0

# display menu and calculated results
print()
print("                                   E - Z    L - O - A - N\n")
print("   Loan: ${:>11,.2f}                                       Monthly Payment: ${:>11,.2f}".format(amount,MP))
print("   APR:   {:>11,.2f} %                                     Total Interest:  ${:>11,.2f}".format(apr,TI))
print("   Term:  {:>11,} months                                Total Cost:      ${:>11,.2f}".format(num_months,TC))
print()
print(" ----- ---------- Payment ----------- ------------- ---------------- Total ----------------")
print("| Mo  | Payment  Principal Interest  |   Balance   |  Payments     Principal    Interest   |")
print("| --- | -------  --------  --------  | ----------  | -----------  -----------  ----------- |")

# loops displaying months based on count being less than the entered term
while count <= num_months:
    payment, principal, interest, amount = loan_calc.apply_payment(MP, amount, apr)

    new_payment += payment
    new_principal += principal
    new_intrest += interest

    print("|{:>4} |  {:,.2f}    {:6,.2f}{:>10,.2f}  |{:>11,.2f}  |{:>12,.2f}{:>13,.2f}{:>13,.2f} |".format(count,payment,principal,interest,amount,new_payment,new_principal,new_intrest))
    count += 1
print(" ----- ------------------------------ ------------- ---------------------------------------")
print()
