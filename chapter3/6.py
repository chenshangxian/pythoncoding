month = int(input("Enter the month (numeric form): "))
day = int(input("Enter the day: "))
year = int(input("Enter the two-digit year: "))

product = month * day

if product == year:
    print("The date is magic!")
else:
    print("The date is not magic.")