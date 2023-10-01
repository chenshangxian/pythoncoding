def main():
    Number_Analysis_program=[]
    for Number in range(1, 21):
        number= float(input(f"Enter the Number for {Number}: "))
        Number_Analysis_program.append(number)
    highest_number=max(Number_Analysis_program)
    lowest_number=min(Number_Analysis_program)
    The_total_of_the_numbers=sum(Number_Analysis_program)
    The_average_of_the_numbers=sum(Number_Analysis_program)/len(Number_Analysis_program)
    print("The numbers are",Number_Analysis_program)
    print("The highest number is",highest_number)
    print("The lowest number is",lowest_number)
    print("The total of the numbers",The_total_of_the_numbers)
    print("The average of the numbers is",The_average_of_the_numbers)
main()