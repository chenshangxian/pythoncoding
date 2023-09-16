def population_growth(starting_population, daily_increase, days):
    current_population = starting_population
    print("Day\tApproximate Population")
    for day in range(1, days + 1):
        print(f"{day}\t{current_population:.5f}")
        current_population += current_population * (daily_increase / 100)
        
starting_organisms = float(input("Enter the starting number of organisms: "))
average_daily_increase = float(input("Enter the average daily population increase (as a percentage): "))
number_of_days = int(input("Enter the number of days the organisms will be left to multiply: "))

population_growth(starting_organisms, average_daily_increase, number_of_days) 