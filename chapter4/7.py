def calculate_pay(days):
    total = 0
    salary = 1 

    print("Day\tSalary($)")
    print("----------------")

    for day in range(1, days + 1):
        print(f"{day}\t{salary:.2f}")
        total += salary
        salary *= 2  
    return total

days = int(input("Enter the number of days: "))
total_pay = calculate_pay(days)

print(f"\nThe total pay at the end of the period is: ${total_pay:.2f}")