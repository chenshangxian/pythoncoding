# File: <NAME OF FILE>
# Description: <A DESCRIPTION OF YOUR PROGRAM>
# Assignment Name and Number: 
#
# Name: <YOUR NAME>
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    mean_radius = { "Io": 1821.6,"Europa": 1560.8,"Ganymede": 2634.1,"Callisto": 2410.3}
    surface_gravity = {"Io": 1.796,"Europa": 1.314,"Ganymede": 1.428,"Callisto": 1.235}
    orbital_period = {"Io": 1.769,"Europa": 3.551,"Ganymede": 7.154,"Callisto": 16.689}
    valid_moons = list(mean_radius.keys())
    moon_name = input("Enter the name of a Galilean moon of Jupiter: ")
    if moon_name in valid_moons:
        print(moon_name,":")
        print(f"Mean Radius:{mean_radius[moon_name]}kilometers")
        print(f"Surface Gravity:{surface_gravity[moon_name]}m/s^2")
        print(f"Orbital Period:{orbital_period[moon_name]}days")
    else:
        print("Invalid moon name!")
main()