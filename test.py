from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Take input from user
user_prompt = input("Enter a prompt for GPT-2 to complete: ")

# Generate text based on the input prompt
result = generator(user_prompt, max_length=100, num_return_sequences=1)

# Display the generated text
print("\nGenerated Text:\n")
print(result[0]['generated_text'])