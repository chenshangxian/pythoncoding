# File: <Calories from Fat and Carbohydrates>
# Description: <It can ask the user to enter a distance in kilometers, then converts that distance to miles. >
# Assignment Name and Number:6. Calories from Fat and Carbohydrates
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
def calories_from_fat(fat_grams):
    return fat_grams * 9
def calories_from_carbs(carb_grams):
    return carb_grams * 4  
def main():
    fat_grams = float(input("Enter the number of fat grams consumed in a day: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed in a day: "))
    
    total_calories_from_fat = calories_from_fat(fat_grams)
    total_calories_from_carbs = calories_from_carbs(carb_grams)
    
    print("The number of calories from carbohydrates is",total_calories_from_fat,"calories.")
    print("The number of calories from carbohydrates is",total_calories_from_carbs,"calories.")

main()
