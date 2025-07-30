from transformers import pipeline

#gpt2
# generator = pipeline('text-generation', model='gpt2')

# user_prompt = input("Enter your prompt: ")

# result = generator(user_prompt, max_length=100, num_return_sequences=1)

# print("\nGenerated Text:\n")
# print(result[0]['generated_text'])

#EleutherAI/gpt-neo-2.7B / t5-base
generator = pipeline('text-generation', model='t5-base')

user_prompt = input("Enter your prompt: ")

result = generator(user_prompt, max_length=100, num_return_sequences=1)

print("\nGenerated Text:\n")
print(result[0]['generated_text'])
