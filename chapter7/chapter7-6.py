import random
def roll(number_of_throws):
    rolls = [random.randint(1, 6) for _ in range(number_of_throws)]
    return sorted(rolls)
def main():
    number_of_throws = int(input("Please enter a positive integer: "))
    print(roll(number_of_throws))
main()
