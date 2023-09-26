def kilometers_to_miles(km):
    return km * 0.6214
def main():
    km = float(input("Enter a distance in kilometers: "))
    miles = kilometers_to_miles(km)
    print(f"{km}kilometers is equal to {miles} miles.")
main()