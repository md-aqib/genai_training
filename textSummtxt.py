from transformers import pipeline
 
def summarize_text(text):

    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')

    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)

    return summary[0]['summary_text']

file_path = input("Enter the path to the text file: ")
 
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    if not text.strip():
        print("The file is empty.")
    else:
        summary = summarize_text(text)
        print("Summarized Text:\n")
        print(summary)
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
