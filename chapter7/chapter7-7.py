# File: <Stadium Seating>
# Description: <It can ask how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.>
# Assignment Name and Number:7. Stadium Seating
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
def main():
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    infile = open('student_answers.txt', 'r')
    student_answers = infile.readlines()
    passed, correct_count, incorrect_answers = check_answers(correct_answers, student_answers)
    if passed:
        print("The student passed!")
    else:
        print("The student failed.")
    print("Total Correctly Answered Questions:",correct_count)
    print("Total Incorrectly Answered Questions:",20 - correct_count)
    print("Questions answered incorrectly:",incorrect_answers)
def check_answers(correct, student):
    correct_count = 0
    incorrect_answers = []

    for i in range(len(correct)):
        if correct[i] == student[i]:
            correct_count += 1
        else:
            incorrect_answers.append(i+1)
    passed = correct_count >= 15
    return passed, correct_count, incorrect_answers
main()
