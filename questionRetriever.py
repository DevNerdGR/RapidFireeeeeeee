from openai import OpenAI
from dotenv import load_dotenv, dotenv_values
from pydantic import BaseModel, TypeAdapter
import os
import json
import enum
import random

load_dotenv()
apiKey = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=apiKey)

with open("categories.json", "r") as f:
    categories = json.loads(f.read())

class question:
    def __init__(self, category, question, answer):
        self.category = category
        self.question = question
        self.answer = answer

class questionModel(BaseModel):
    category : str
    question : str
    answer : str

class QuestionCategory(enum.Enum):
    IO_CONTENT = 0
    ORG_CHEM = 1
    THERMO = 2
    IMMUNOLOGY_AND_PATHOLOGY = 3
    ANATOMY = 4
    MAT_SCI = 5
    ENGINEERING = 6
    LOW_LEVEL_COMP = 7
    P_CHEM = 8
    INORG_CHEM = 9
    ECOLOGY = 10
    GENETICS = 11
    DNA_TECH = 12
    RELATIVITY = 13
    QUANTUM_PHY = 14
    ASTRO = 15

    def randomCategory():
        return random.randrange(0, len(categories))


class QuestionGenerator:
    def __init__(self):
        self.questionHistory = ""
    
    def getQuestion(self, subject) -> question:
        return self.getQuestionAsStructuredResponse(f"generate only ONE {categories[subject]} question fill in the blank style, 1 word answer per question. these questions should be challenging for secondary 3 school students while being doable. The following questions have been given and should not be repeated: {self.questionHistory}")
    
    def getQuestionAsStructuredResponse(self, message : str) -> question:
        response = client.responses.parse(
            model="gpt-5-mini",  
            input=[{"role": "system", "content": message}],
            text_format=questionModel,
        )
        qn = response.output_parsed
        self.questionHistory += qn.question + "\n"
        return question(qn.category, qn.question, qn.answer)
    

if __name__ == "__main__":
    g = QuestionGenerator() 
    print(g.getQuestion(6))