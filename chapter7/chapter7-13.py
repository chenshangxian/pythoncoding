# File: <NAME OF FILE>
# Description: <A DESCRIPTION OF YOUR PROGRAM>
# Assignment Name and Number: 
#
# Name: <YOUR NAME>
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def read_responses(filename):
    with open(filename, 'r') as file:
        responses = file.readlines()
    return [response.strip() for response in responses]
def magic_8_ball(responses):
    while True:
        question = input("Ask the Magic 8 Ball a yes or no question (or press Enter to quit): ")
        if not question:
            break
        if input("Shake the Magic 8 Ball? (Press Enter to shake, or type 'quit' to exit): ").strip().lower() == 'quit':
            break
        else:
            random_response = random.choice(responses)
            print(f"You asked: {question}")
            print(f"Magic 8 Ball says: {random_response}\n")
responses = read_responses("/Users/VincentChen/Desktop/8_ball_responses.txt")
if responses:
    print("Welcome to the Magic 8 Ball!")
    magic_8_ball(responses)
else:
    print("The Magic 8 Ball cannot provide answers without responses. Please check the file and try again.")