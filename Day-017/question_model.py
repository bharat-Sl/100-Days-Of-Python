class QuestionModel:

    def __init__(self,question,correct_answer):
        self.question=question
        self.correct_answer=correct_answer

    def check(self,user_answer):
        if(user_answer==self.correct_answer):
            return True
        else:
            return False

    def get_answer(self,answer):
        if(self.check(answer)):
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.correct_answer}.")