# File: <Magic 8 Ball>
# Description: <It can read the responses from the file into a list.Prompt the user to ask a question, then display one of the responses, randomly selected from the list.Repeat until the user is ready to quit.>
# Assignment Name and Number:13.Magic 8 Ball
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def read_responses(filename):
    infile = open(filename, 'r')
    answer_list = []
    for i in range(12):
        line = infile.readline()
        line = line.rstrip("\n")
        answer_list.append(line)
    infile.close()
    return answer_list
def magic_8_ball(responses):
    question = input("Ask the Magic 8 Ball a yes or no question (or press Enter to quit): ")
    while question != "quit":
        random_response = random.choice(responses)
        print("You asked:", question)
        print("Magic 8 Ball says:",random_response)
        question = input("Ask the Magic 8 Ball a yes or no question (or press Enter to quit): ")
responses = read_responses("8_ball_responses.txt")
if responses:
    print("Welcome to the Magic 8 Ball!")
    magic_8_ball(responses)
else:
    print("The Magic 8 Ball cannot provide answers without responses. Please check the file and try again.")