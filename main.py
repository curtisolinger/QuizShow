# Import the Question class which contains two attributes: questions text and question answer
from question_model import Question
# Import a list of dictionaries that contain quiz questions and answers
from data import question_data
# Import the QuizBrain class that has three attributes: question number, question list, and the score
# It also has three methods: still_has_question, 
from quiz_brain import QuizBrain

# Declare a list that will contain Question objects
question_bank = []

for question in question_data:
    # Extract the question from the dictionary
    question_text = question["text"]
    # Extract the answer from the dictionary
    question_answer = question["answer"]
    # Create a new Question object with the question text and answer
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # Append the new Question object to the question_bank list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
