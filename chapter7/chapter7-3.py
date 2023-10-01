def main():
    monthly_rainfall = []
    for month in range(1, 13):
        rainfall = float(input(f"Enter the total rainfall for month {month}: "))
        monthly_rainfall.append(rainfall)
    total_rainfall = sum(monthly_rainfall)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(monthly_rainfall)
    min_rainfall = min(monthly_rainfall)
    month_max_rainfall = monthly_rainfall.index(max_rainfall) + 1 
    month_min_rainfall = monthly_rainfall.index(min_rainfall) + 1 
    print("\nRainfall Statistics:")
    print("Total rainfall for the year: ",total_rainfall,"inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with the highest rainfall: Month {month_max_rainfall} with {max_rainfall} inches")
    print(f"Month with the lowest rainfall: Month {month_min_rainfall} with {min_rainfall} inches")
main()
