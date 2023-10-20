import random
def main():
    states_and_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise','Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines','Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge','Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston','Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson','Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln','Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton','New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville','Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier','Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston','Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    correct_count = 0
    incorrect_count = 0
    while True:
        state = random.choice(list(states_and_capitals.keys()))
        capital = states_and_capitals[state]
        user_answer = input(f"What is the capital of {state}? ")
        if user_answer== capital:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Sorry, the correct answer is {capital}.")
            incorrect_count += 1
        another = input("Do you want another question? (yes/no) ")
        if another != 'yes':
            break
    print(f"You answered {correct_count} questions correctly and {incorrect_count} incorrectly.")
main()
