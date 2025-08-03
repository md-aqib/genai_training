# 1. Code Generation: 
# 	Problem Statement: Insurance companies require an efficient solution for generating premium calculation code. The proposed tool addresses this need:
# 	Objective: Develop a Python script using the Groq API to automatically generate insurance premium calculation code.
# 	Key Features: 
#             1. User input for specific calculation parameters 
#             2. Automated code generation via Groq API 
#             3. Flexible accommodation of various insurance products 
# 	Target Users: Insurance actuaries and developers, without requiring deep programming knowledge

import os
import requests
from dotenv import load_dotenv

load_dotenv()

groqApiKey = os.getenv("GROQ_API_KEY")
print("MMMM", groqApiKey)
groqApiUrl = "https://api.groq.com/openai/v1/chat/completions"

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

    headers = {
        "Authorization": f"Bearer {groqApiKey}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who writes simple insurance-related Python functions."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    res = requests.post(groqApiUrl, headers=headers, json=data)
    res.raise_for_status()

    return res.json()["choices"][0]["message"]["content"]

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