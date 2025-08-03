# 3. Code Generation
# Problem Statement:
# We need a Python script that uses the Groq API to generate code snippets for banking applications. The script should:
#     1. Prompt the User: Ask the user to describe a banking-related coding task they need help with. For example, calculating monthly interest or managing transactions.
#     2. Generate Code: Use the Groq API to create a Python function based on the user's description. The API will provide code snippets tailored to the specific task.
#     3. Display Results: Show the generated code to the user so they can review and use it for their banking application.
# Example User Prompts:
#     • "Write a Python function to calculate the monthly interest on a savings account."
#     • "Create a function to handle deposits and withdrawals in a checking account."
#     • "Implement a function to generate a bank statement for a given period."

import os
import requests
from dotenv import load_dotenv

load_dotenv()

groqApiKey = os.getenv("GROQ_API_KEY")
groqApiUrl = "https://api.groq.com/openai/v1/chat/completions"
modelName = "llama-3.1-8b-instant"

def getUserPrompt():
    print("\nPlease enter a banking-related coding task.")
    print("Examples:")
    print("• Write a Python function to calculate the monthly interest on a savings account.")
    print("• Create a function to handle deposits and withdrawals in a checking account.")
    print("• Implement a function to generate a bank statement for a given period.")
    return input("Enter your prompt (or type 'exit' to quit): ").strip()

def generateBankingCode(userPrompt):
    headers = {
        "Authorization": f"Bearer {groqApiKey}",
        "Content-Type": "application/json"
    }

    data = {
        "model": modelName,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates clean Python code for banking applications."},
            {"role": "user", "content": f"Write Python code for the following banking task: {userPrompt}. Add helpful comments."}
        ],
        "temperature": 0.4
    }

    try:
        res = requests.post(groqApiUrl, headers=headers, json=data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as httpErr:
        print("HTTP Error:", httpErr)
        print("Response:", res.text)
    except Exception as e:
        print("Unexpected error:", e)
    return None

def runBankingTool():
    print("Welcome to the Banking Code Generator using Groq API")
    while True:
        userPrompt = getUserPrompt()
        if userPrompt.lower() in ['exit',]()
