from question_model import Question_model
from data import question_data
from quiz_brain import Quiz_brain
question_bank=[]
for item in question_data:
    question_bank.append(Question_model(item["text"],item["answer"]))

quiz=Quiz_brain(question_bank)
print(quiz.next_question())

while quiz.still_has_question():
    quiz.next_question()

print('Game is over')
print(f'Your total score was {quiz.score}/{quiz.question_number}')

