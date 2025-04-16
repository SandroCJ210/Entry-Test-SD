from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from .trivia import Question, Quiz
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

quiz = Quiz()

class QuestionRequest(BaseModel):
    description: str
    options: List[str]
    correct_answer: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/questions/", status_code=status.HTTP_201_CREATED)
def add_question(question_req: QuestionRequest):
    question = Question(
        description=question_req.description,
        options=question_req.options,
        correct_answer=question_req.correct_answer
    )
    quiz.add_question(question)
    return {"message": "Pregunta agregada exitosamente"}

@app.post("/questions/restart")
def restart_quiz(difficulty: int = 1):
    quiz.questions.clear()
    quiz.correct_answers = 0
    quiz.incorrect_answers = 0
    quiz.current_question_index = 0
    quiz.load_questions(difficulty)
    return {"message": f"Trivia reiniciada con dificultad {difficulty}"}