# File: <Rock, Paper, Scissors Game>
# Description: <It canlet the user play the game of Rock, Paper, Scissors against the computer.>
# Assignment Name and Number:21. Rock, Paper, Scissors Game
#
# Name: <Vincent Chen>
# GitHub: <https://github.com/chenshangxian/pythoncoding>
#
# On my honor, <Vincent Chen>, this programming assignment is my own work
# and I have not provided this code to any other student.
import random
def get_computer_choice():
    choice = random.randint(1, 3)
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    else:
        return 'scissors'
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'user'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    else:
        return 'computer'
def main():
    computer_choice = get_computer_choice()
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    print("The computer chose:" ,computer_choice,)
    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie! Play again.")
    elif winner == 'user':
        print("Congratulations, you win!")
    else:
        print("Sorry, the computer wins.")
main()
