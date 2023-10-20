# File: <Valid Number Information>
# Description: <It filters numbers from the list numbers that are within the range of 0 to 100. It then calculates the sum and average of these valid numbers and prints the results.>
# Assignment Name and Number:  1:Valid Number Information
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
for number in numbers:
    if 0 <= number <= 100:
        valid_numbers.append(number)
total = sum(valid_numbers)
average = total / len(valid_numbers)
print("Valid numbers:", valid_numbers)
print("Total:", total)
print("Average:", average)