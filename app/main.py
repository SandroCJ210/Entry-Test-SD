from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from .trivia import Question, Quiz
app = FastAPI()


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
    quiz = Quiz()
    question = Question(
        description=question_req.description,
        options=question_req.options,
        correct_answer=question_req.correct_answer
    )
    quiz.add_question(question)
    return {"message": "Pregunta agregada exitosamente"}