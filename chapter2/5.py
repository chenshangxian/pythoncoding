def calculate_distance(speed, time):
    return speed * time

def main():
    speed = 70

    time_6_hours = 6
    time_10_hours = 10
    time_15_hours = 15

    distance_6_hours = calculate_distance(speed, time_6_hours)
    distance_10_hours = calculate_distance(speed, time_10_hours)
    distance_15_hours = calculate_distance(speed, time_15_hours)

    print(f"The distance the car will travel in 6 hours: {distance_6_hours}英里")
    print(f"The distance the car will travel in 10 hours: {distance_10_hours}英里")
    print(f"The distance the car will travel in 15 hours: {distance_15_hours}英里")

    main()