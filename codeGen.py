import groq
from dotenv import load_dotenv
import os
 
def code_generator(prompt):
    # Directly input the API key
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")  # Replace with your actual Groq API key
    print("MMMM", api_key)
    # Initialize the Groq client
    client = groq.Groq(api_key=api_key)
 
    # Generate code based on the prompt using the Groq chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",  # Example model, update as per your Groq setup
        max_tokens=200,
    )
 
    # Extract the generated code from the response
    generated_code = chat_completion.choices[0].message.content
 
    return generated_code
 
# Main execution
user_input = input("Enter a prompt: ")
generated_code = code_generator(user_input)
 
# Print the generated code
print("Generated Code:\n")
print(generated_code)
 
#python code for fibonacci series
#java code for fibonacci series