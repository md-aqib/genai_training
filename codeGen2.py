# 2. Code Generation:
# Problem Statement:
# 	Develop a Python-based code generator that assists developers in generating Python code snippets specifically tailored for retail applications. The code generator should utilize the Groq API for generating code based on user-provided prompts. The goal is to create an interactive tool that helps users input various retail-related coding tasks (e.g., managing sales, inventory systems, or customer discounts) and returns relevant Python code solutions.
# 	Key Requirements:
#     1. API Integration: The system must integrate with the Groq API to leverage AI-based code generation, using the provided API key for authentication.
#     2. User Interaction: The application should interactively prompt the user to input retail-related coding tasks, offering examples to guide them. It must also allow users to exit the tool gracefully when done.
#     3. Code Generation: Based on the user's prompt, the system should generate Python code that addresses the retail-related functionality described in the prompt. This could include tasks such as calculating sales, managing customer discounts, or handling inventory.
#     4. Customizable Prompts: Users should be able to input their own prompts, and the AI should respond with corresponding code solutions. The system must handle user input dynamically.
#     5. Error Handling: The system should handle potential errors such as invalid API key usage or incomplete responses from the Groq API.


import os
from dotenv import load_dotenv
import groq

load_dotenv()

apiKey = os.getenv("GROQ_API_KEY")
modelName = "llama-3.1-8b-instant"

client = groq.Groq(api_key=apiKey)

def getRetailPrompt():
    print("\nEnter a retail-related Python coding task you need help with.")
    print("Examples:")
    print("- Calculate total bill after applying discount and tax")
    print("- Create inventory management system")
    print("- Track customer purchase history\n")
    userPrompt = input("Your prompt (or type 'exit' to quit): ")
    return userPrompt.strip()

def generateRetailCode(userPrompt):
    try:
        chatCompletion = client.chat.completions.create(
            model=modelName,
            max_tokens=400,
            temperature=0.4,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that generates clean Python code for retail applications."
                },
                {
                    "role": "user",
                    "content": f"Write Python code for the following retail task: {userPrompt}. Add helpful comments in the code."
                }
            ]
        )
        return chatCompletion.choices[0].message.content
    except Exception as e:
        print("Error:", str(e))
        return None

def startInteractiveTool():
    print("Welcome to the Retail Code Generator Tool using Groq API!")
    while True:
        userPrompt = getRetailPrompt()
        if userPrompt.lower() in ['exit', 'quit']:
            print("Exiting...")
            break

        print("\nGenerating code... please wait...\n")
        generatedCode = generateRetailCode(userPrompt)

        if generatedCode:
            print("Here's your generated Python code:\n")
            print(generatedCode)
        else:
            print("Could not generate code. Please check your prompt or API key.")

startInteractiveTool()

