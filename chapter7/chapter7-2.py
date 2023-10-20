# File: <Lottery Number Generator>
# Description: <Generate and print a 7-digit lottery number with each digit as a random integer from 0 to 9>
# Assignment Name and Number:2.Lottery Number Generator
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def generate_lottery_number():
    lottery_numbers = [random.randint(0, 9) for i in range(7)]
    for number in lottery_numbers:
        print(number, end='')
    print()
generate_lottery_number()