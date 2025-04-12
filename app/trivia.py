class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
def run_quiz(quiz: Quiz):    
    print("¡Bienvenid@ a la trivia! Comencemos con las preguntas.")
    questions = quiz.questions
    for i in range(len(questions)):
        question = quiz.get_next_question()
        print("Pregunta ", i+1)
        print(question.description)
        for j in range(len(question.options)):
            print(chr(97+j), ")", question.options[j])

quiz = Quiz()
question = Question("¿Cuánto es 1+1?", [3, 6, 4, 2], 4)
quiz.add_question(question)
run_quiz(quiz)