# File: <Kilometer Converter>
# Description: <It can ask the user to enter a distance in kilometers, then converts that distance to miles. >
# Assignment Name and Number:1. Kilometer Converter
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
def kilometers_to_miles(km):
    return km * 0.6214
def main():
    km = float(input("Enter a distance in kilometers: "))
    miles = kilometers_to_miles(km)
    print(f"{km}kilometers is equal to {miles} miles.")
main()