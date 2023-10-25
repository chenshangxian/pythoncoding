# File: <Paint Job Estimator>
# Description: <It can ask the user to enter the square feet of wall space to be painted and the price of the paint per gallon. >
# Assignment Name and Number:8. Paint Job Estimator
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    SQ_FEET_PER_GALLON = 112
    LABOR_HOURS_PER_GALLON = 8
    LABOR_COST_PER_HOUR = 35.00
    def calculate_paint_required(sq_feet):
        return sq_feet / SQ_FEET_PER_GALLON
    def calculate_labor_hours(sq_feet):
        return (sq_feet / SQ_FEET_PER_GALLON) * LABOR_HOURS_PER_GALLON
    def calculate_paint_cost(gallons, paint_price_per_gallon):
        return gallons * paint_price_per_gallon
    def calculate_labor_cost(labor_hours):
        return labor_hours * LABOR_COST_PER_HOUR
    sq_feet = float(input("Enter the square feet of wall space to be painted: "))
    paint_price_per_gallon = float(input("Enter the price of paint per gallon: "))
    gallons_required = calculate_paint_required(sq_feet)
    labor_hours_required = calculate_labor_hours(sq_feet)
    paint_cost = calculate_paint_cost(gallons_required, paint_price_per_gallon)
    labor_cost = calculate_labor_cost(labor_hours_required)
    print("Number of gallons of paint required: ",gallons_required)
    print("Hours of labor required: ",labor_hours_required)
    print("Cost of the paint: $",paint_cost)
    print("Labor charges: $",labor_cost)
    total_cost = paint_cost + labor_cost
    print("Total cost of the paint job: $",total_cost)
main()