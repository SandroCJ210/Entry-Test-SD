import json

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
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
    def load_questions(self, difficulty_number: int = 1, json_path: str = "app/questions.json"):
        difficulty = ""

        if(difficulty_number == 1):
            difficulty = "easy"
        elif(difficulty_number == 2):
            difficulty = "medium"
        elif(difficulty_number == 3):
            difficulty = "hard"
        
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            questions_data = data.get(difficulty.lower(), [])
            for q in questions_data:
                question = Question(
                    description=q["description"],
                    options=q["options"],
                    correct_answer=q["correct_answer"]
                )
                self.add_question(question)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error cargando preguntas: {e}")

    
def run_quiz(quiz: Quiz):    
    print("¡Bienvenid@ a la trivia de la serie Invincible! Comencemos con las preguntas.")
    difficulty = int(input("Ingrese la dificultad con la que quiere jugar: \n1. Fácil.\n2. Media.\n3. Difícil\n"))
    quiz.load_questions(difficulty)
    questions = quiz.questions

    for i in range(10):
        question = quiz.get_next_question()

        if(question is None):
            break

        print("Pregunta ", i+1)
        print(question.description)

        for j in range(len(question.options)):
            print(chr(97+j), ")", question.options[j])
        
        answer = input("Rpta.: ")
        result = quiz.answer_question(question, answer)
        mensaje = "La respuesta es correcta." if result else "La respuesta es incorrecta."
        print(mensaje)
    
    print("Tienes ", quiz.correct_answers, " respuestas correctas y \n", quiz.incorrect_answers, "respuestas incorrectas.")
    

def main():
    quiz = Quiz()
    run_quiz(quiz)

if __name__=="__main__":
    main()