def calculate_calories_burned(minutes):
    calories_per_minute = 4.2
    return minutes * calories_per_minute
for time in [10, 15, 20, 25, 30]:
    calories = calculate_calories_burned(time)
    print("After",time, "minutes", "you have burned",calories,)