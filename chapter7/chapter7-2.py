import random
def generate_lottery_number():
    lottery_numbers = [random.randint(0, 9) for _ in range(7)]
    for number in lottery_numbers:
        print(number, end='')
    print()
generate_lottery_number()