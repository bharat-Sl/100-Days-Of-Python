#Project Day17

from question_model import QuestionModel
from quiz_brain import QuizBrain
from Data import question_data


quiz=QuizBrain()
for question in question_data:
    if(quiz.status):
        model=QuestionModel(question["text"],question["answer"])
        ans=input(f"{model.question} (True/False): ").title()
        model.get_answer(ans)
        quiz.update(model.check(ans))