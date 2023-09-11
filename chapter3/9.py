def main():
    pocket_number = int(input("Enter a pocket number (0 through 36): "))
    if pocket_number == 0:
        print("The pocket is green.")
    elif pocket_number >= 1 and pocket_number <= 10:
        if pocket_number % 2 == 0:
            print("The pocket is black.")
        else:
            print("The pocket is red.")
    elif pocket_number >= 11 and pocket_number <= 18:
        if pocket_number % 2 == 0:
            print("The pocket is red.")
        else:
            print("The pocket is black.")
    elif pocket_number >= 19 and pocket_number <= 28:
        if pocket_number % 2 == 0:
            print("The pocket is black.")
        else:
            print("The pocket is red.")
    elif pocket_number >= 29 and pocket_number <= 36:
        if pocket_number % 2 == 0:
            print("The pocket is red.")
        else:
            print("The pocket is black.")
    else:
        print("Error: Enter a pocket number between 0 and 36.")

main()