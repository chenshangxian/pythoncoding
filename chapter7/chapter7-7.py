def main():
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    with open('/Users/VincentChen/Desktop/student_answers.txt') as file:
        student_answers = file.readlines()
    student_answers = [answer.strip() for answer in student_answers]
    passed, correct_count, incorrect_answers = check_answers(correct_answers, student_answers)
    if passed:
        print("The student passed!")
    else:
        print("The student failed.")
    print(f"Total Correctly Answered Questions: {correct_count}")
    print(f"Total Incorrectly Answered Questions: {20 - correct_count}")
    print(f"Questions answered incorrectly: {incorrect_answers}")
def check_answers(correct, student):
    correct_count = 0
    incorrect_answers = []

    for i, (c, s) in enumerate(zip(correct, student)):
        if c == s:
            correct_count += 1
        else:
            incorrect_answers.append(i+1)
    
    passed = correct_count >= 15
    return passed, correct_count, incorrect_answers

main()
