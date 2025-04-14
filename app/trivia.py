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

    
def run_quiz(quiz: Quiz):    
    print("¡Bienvenid@ a la trivia de la serie Invincible! Comencemos con las preguntas.")
    questions = quiz.questions

    for i in range(10):
        question = quiz.get_next_question()

        print("Pregunta ", i+1)
        print(question.description)

        for j in range(len(question.options)):
            print(chr(97+j), ")", question.options[j])
        
        answer = input("Rpta.: ")
        result = quiz.answer_question(question, answer)
        mensaje = "La respuesta es correcta." if result else "La respuesta es incorrecta."
        print(mensaje)
    
    print("Tienes ", quiz.correct_answers, " respuestas correctas y \n", quiz.incorrect_answers, "respuestas incorrectas.")
    

def setQuestions(quiz: Quiz):
    question = Question("¿Cómo se llama el protagonista de la serie?", ["Nolan Grayson", "William Clockwell", "Mark Grayson", "Allen el Alien"], "Mark Grayson")
    quiz.add_question(question)

    question = Question("¿Cuál es el nombre de superhéroe de Mark?", ["Omni-Man", "Atom Boy", "Guardian", "Invincible"], "Invincible")
    quiz.add_question(question)

    question = Question("¿Quién es el padre de Mark y también un superhéroe?", ["Cecil Stedman", "Allen el Alien", "Nolan Grayson", "Donald Ferguson"], "Nolan Grayson")
    quiz.add_question(question)

    question = Question("¿Cómo se llama la madre de Mark?", ["Amber Bennett", "Debbie Grayson", "Eve Wilkins", "Samantha Eve"], "Debbie Grayson")
    quiz.add_question(question)

    question = Question("¿Qué poder tiene Atom Eve?", ["Superfuerza", "Invisibilidad", "Manipulación de la materia y energía", "Control del tiempo"], "Manipulación de la materia y energía")
    quiz.add_question(question)

    question = Question("¿Cómo se llama el mejor amigo de Mark?", ["Rex Splode", "William Clockwell", "Cecil Stedman", "Allen el Alien"], "William Clockwell")
    quiz.add_question(question)

    question = Question("¿Qué equipo de superhéroes es destruido por Omni-Man en el primer episodio?", ["Guardianes del Globo", "Los Vengadores", "Liga de la Justicia", "Guardianes de la Galaxia"], "Guardianes del Globo")
    quiz.add_question(question)

    question = Question("¿Qué especie alienígena es Omni-Man?", ["Kryptoniano", "Viltrumita", "Namekiano", "Saiyajin"], "Viltrumita")
    quiz.add_question(question)

    question = Question("¿Cómo se llama la novia de Mark durante la primera temporada?", ["Eve Wilkins", "Debbie Grayson", "Amber Bennett", "Tara"], "Amber Bennett")
    quiz.add_question(question)

    question = Question("¿Qué personaje extraterrestre desafía a Mark en un combate de prueba?", ["Allen el Alien", "Thokk", "Battle Beast", "Thragg"], "Allen el Alien")
    quiz.add_question(question)



def main():
    quiz = Quiz()
    setQuestions(quiz)
    run_quiz(quiz)

if __name__=="__main__":
    main()