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
