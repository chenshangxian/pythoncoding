class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, correct_ans_no):
        self.__question = question
        self.__answers1 = ans1
        self.__answers2 = ans2
        self.__answers3 = ans3
        self.__answers4 = ans4
        self.__correct_ans_no = correct_ans_no
    def get_question(self):
        return self.__question
    def get_answers(self):
        return [self.__answers1,self.__answers2,self.__answers3,self.__answers4,]
    def get_correct_answer(self):
        return self.__correct_ans_no
def create_questions():
    q1 = Question("Who is Crespi's teacher?", "Mr.Dwyer", "Dr.Bengford", "Mr.Lopez", "Mrs.Yang", 3)
    q2 = Question("Which classroom is mathematic room?", "12", "1", "22", "17", 3)
    q3 = Question("Which is Kevin's Chinese name?", "Zhouyibo", "Wilson", "Liuzitao", "Kevin", 3)
    q4 = Question("Who is the current President of the United States?", "Richard M. Nixon", "Barack Hussein Obama", "Joseph Robinette Biden Jr.", "Donald John Trump", 3)
    q5 = Question("What is the middle letter of celts?", "c", "s", "t", "l", 4)

    return [q1, q2, q3, q4, q5] * 2 
    
def main():
    questions_list = create_questions()
    players = ["Player 1", "Player 2"]
    scores = [0, 0]

    for i in range(2):
        print("It's",players[i],"s turn!")
        for j in range(5):
            print(questions_list[j].get_question())
            answers = questions_list[j].get_answers()
            for k in range(1,5):
                print(k,":",answers[k-1])
            ans_player=int(input("Please input your answer"))
            if(ans_player==questions_list[j].get_correct_answer()):
                scores[i]+=1

    print("\nScores:")
    for i in range(2):
        print("player",i+1,"gets",scores[i],"points")

    if scores[0] > scores[1]:
        print("Player 1 wins!")
    elif scores[0] < scores[1]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
main()