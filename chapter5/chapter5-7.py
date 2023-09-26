def income_from_class_a(tickets_sold):
    return tickets_sold * 20
def income_from_class_b(tickets_sold):
    return tickets_sold * 15
def income_from_class_c(tickets_sold):
    return tickets_sold * 10
def total_income(a_income, b_income, c_income):
    return a_income + b_income + c_income
def main():
    tickets_a = int(input("Please enter the number of tickets sold for Class A seats: "))
    tickets_b = int(input("Please enter the number of tickets sold for Class B seats: "))
    tickets_c = int(input("Please enter the number of tickets sold for Class C seats: "))
    income_a = income_from_class_a(tickets_a)
    income_b = income_from_class_b(tickets_b)
    income_c = income_from_class_c(tickets_c)
    total = total_income(income_a, income_b, income_c)
    print("The total income generated from ticket sales is: $",total,)
main()