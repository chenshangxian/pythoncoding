# File: <Kinetic Energy>
# Description: <It can return the amount of kinetic energy that the object has>
# Assignment Name and Number:14. Kinetic Energy
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
def kinetic_energy(mass, velocity):
    KE = 0.5 * mass * velocity**2
    return KE
def main():
    mass = float(input("Please enter the object's mass in kilograms: "))
    velocity = float(input("Please enter the object's velocity in meters per second: "))
    KE = kinetic_energy(mass, velocity)
    print(f"The object's kinetic energy is: {KE:.2f} Joules.")
main()
