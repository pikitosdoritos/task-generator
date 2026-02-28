from dotenv import load_dotenv
from google import genai
import json
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in environment variables")

client = genai.Client(api_key=API_KEY)

res = {}
first_prompt = []

task_categories = [
    "Turn-based games",
    "Dynamic games",
    "Converters",
    "Editors",
    "Presentations",
    "Pure functions",
    "Reimplementations",
    "Classes",
    "Template engines",
    "Record managers",
    "Servers",
    "API",
    "API clients",
    "Visualizations",
    "Frameworks",
    "Components",
    "Libraries",
    "Modules",
    "Using third-party solutions",
    "Data services",
    "Landing pages",
    "Stores",
    "Coding layouts",
    "Proof-of-concept examples",
    "Data generators",
    "Service clones",
    "Emulations",
    "Bots",
    "File managers",
    "Schedulers",
    "Organizers",
    "Statistics and data analysis",
    "Galleries",
    "Communication",
    "Documentation",
    "Tests",
    "Builds",
    "Builders, bundlers",
    "Extensions",
    "Audio",
    "Video",
    "Task-management",
    "Refactoring",
    "Search, bug fixing",
    "Reading and explaining code",
    "Templates",
    "Thematic research",
    "Articles",
    "Reports",
    "Integration",
    "Automation",
    "Layouts",
    "Styling",
    "Architectural design"
]

difficulties = [
    "Easy",
    "Medium",
    "Hard"
]

languages = [
"Python", 
"Java",
"C++",
"C#",
"Go",
"Rust",
"JavaScript",
"TypeScript",
"Kotlin",
"Swift",
"PHP",
"Ruby",
"Dart",
"Scala",
]

def choose_task_category():
    for index, item in enumerate(task_categories, start=1):
        print(f"{index}. {item}")
    task_category = input("Choose a task category(enter the number from 1 to 53): ")
    if task_category.isdigit() and 1 <= int(task_category) <= 53:
        first_prompt.append(task_categories[int(task_category) - 1])

def choose_difficulty():
    for index, item in enumerate(difficulties, start=1):
        print(f"{index}. {item}")
    difficulty = input("Choose a difficulty(enter the number from 1 to 3): ")
    if difficulty.isdigit() and 1 <= int(difficulty) <= 3:
        first_prompt.append(difficulties[int(difficulty) - 1])

def choose_language():
    for index, item in enumerate(languages, start=1):
        print(f"{index}. {item}")
    language = input("Choose a language(enter the number from 1 to 15): ")
    if language.isdigit() and 1 <= int(language) <= 15:
        first_prompt.append(languages[int(language) - 1])
        
def send_prompt(first_prompt):
    category = first_prompt[0]
    difficulty = first_prompt[1]
    language = first_prompt[2]
    
    prompt = f"""
You are a senior software architect.

Project parameters:
Category: {category}
Difficulty: {difficulty}
Language: {language}

Generate 5 clarification questions.

Return STRICTLY in JSON format like this:

{{
  "questions": [
    "Question 1",
    "Question 2",
    "Question 3"
  ]
}}

Do not write anything except JSON.
"""
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    return response.text

while True:
    choose_task_category()
    choose_difficulty()
    choose_language()

    print(f"You have chosen: \ncategory: {first_prompt[0]}, \ndifficulty: {first_prompt[1]}, \nlanguage: {first_prompt[2]}")
    
    result = send_prompt(first_prompt)
    print("\nWait for response!")
    print(result)
    
    break