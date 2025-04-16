from locust import HttpUser, task

class TriviaUser(HttpUser):
    @task
    def create_question(self):
        example_question = {
            "description": "¿Cuál es la capital de Francia?",
            "options": ["Madrid", "París", "Londres", "Berlín"],
            "correct_answer": "París"
        }

        self.client.post("/questions/", json=example_question)