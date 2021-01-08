class QuizBrain:
    def __init__(self):
        self.score=0
        self.question=0
        self.status=True
    def update(self,check):
        if(self.question<=10):
            self.question+=1
            if(check==True):
                self.score+=1
            print(f'Your current score is: {self.score}/{self.question}')
        else:
            self.status=False
            print("You've completed the quiz")
            print(f"Your final score was:{self.score}/{self.question}")
        return self.status