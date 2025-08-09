# 1. Code Generation: 
# 	Problem Statement: Insurance companies require an efficient solution for generating premium calculation code. The proposed tool addresses this need:
# 	Objective: Develop a Python script using the Groq API to automatically generate insurance premium calculation code.
# 	Key Features: 
#             1. User input for specific calculation parameters 
#             2. Automated code generation via Groq API 
#             3. Flexible accommodation of various insurance products 
# 	Target Users: Insurance actuaries and developers, without requiring deep programming knowledge

#USING BOTH GRQ API and GROQ PACKAGE
import os
# import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groqApiKey = os.getenv("GROQ_API_KEY")
print("MMMM", groqApiKey)
modelName = "llama-3.1-8b-instant"
# groqApiUrl = "https://api.groq.com/openai/v1/chat/completions"

client = Groq(api_key=groqApiKey)

def generatePremiumCode(params):
    prompt = f"""
    Write a Python function to calculate the insurance premium for the following:
    Product Type: {params['product_type']}
    Age: {params['age']}
    Gender: {params['gender']}
    Term: {params['term']}
    Sum Assured: ₹{params['sum_assured']}

    Extra Details: {params.get('description', 'None')}
    
    Use basic logic and add some comments to explain the steps.
    """

    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant who writes simple insurance-related Python functions."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "model": modelName,
        "max_tokens": 400
    }

    # headers = {
    #     "Authorization": f"Bearer {groqApiKey}",
    #     "Content-Type": "application/json"
    # }
    # chat_completion = requests.post(groqApiUrl, headers=headers, json=data)
    # chat_completion.raise_for_status()
    # return chat_completion.json()["choices"][0]["message"]["content"]

    chat_completion = client.chat.completions.create(**data)
    return chat_completion.choices[0].message.content

userInput = {
    "product_type": "Health Insurance",
    "age": 28,
    "gender": "Female",
    "term": 15,
    "sum_assured": 500000,
    "description": "Basic coverage for hospital expenses with minor age factor."
}

generatedCode = generatePremiumCode(userInput)
print("\nGenerated Code:\n")
print(generatedCode)