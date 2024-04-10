from openai import OpenAI
import os

class Summarizer:

    def __init__(self):
        self.client = OpenAI()
        os.environ["OPENAI_API_KEY"] = ''

    def summarize(self, text, isQuestion=True):
        tag = "question" if isQuestion else "answer"
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": 
                        "You are a fianacial analyst reading earnings call transcript, skilled in analyzing the call and perform summarization. Your task is to summartize the questions and answers concisely."},
                {"role": "user", "content": f"Summarize this {tag}: {text}"}
            ]
        )
        return completion.choices[0].message.content