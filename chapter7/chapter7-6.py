# File: <Dice Rolling Function>
# Description: <It can generate and return a sorted list of number_of_throws random numbers between 1 and 6.Prompt the user to enter a positive integer that is sent to the function, and then print the returned list.>
# Assignment Name and Number: 6. Dice Rolling Function
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def roll(number_of_throws):
    rolls = [random.randint(1, 6) for _ in range(number_of_throws)]
    return sorted(rolls)
def main():
    number_of_throws = int(input("Please enter a positive integer: "))
    print(roll(number_of_throws))
main()
