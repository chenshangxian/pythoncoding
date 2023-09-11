P = float(input("Enter the principal amount originally deposited into the account: "))
r = float(input("Enter the annual interest rate (as a percentage): ")) / 100
n = int(input("Enter the number of times per year that the interest is compounded: "))
t = float(input("Enter the number of years the account will be left to earn interest: "))

A = P * (1 + r/n)**(n*t)

print(f"The amount of money in the account after {t} years will be ${A:.2f}")
