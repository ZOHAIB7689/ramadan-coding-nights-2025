import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API="GEMINI_API_KEY"
genai.configure(api_key=os.environ[GEMINI_API])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    # Get input from user
    user_question = input("\nEnter your question (or type 'exit' to quit): ")
    
    # Check if user wants to exit
    if user_question.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Generate response based on user input
    response = model.generate_content(user_question)
    
    print(response.text)


