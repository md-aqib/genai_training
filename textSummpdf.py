from transformers import pipeline
import PyPDF2

def summarizeText(text):
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']

file_path = input("Enter the path to the PDF file: ")

try:
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    if not text.strip():
        print("The PDF file is empty or could not be read.")
    else:
        summary = summarizeText(text)
        print("Summarized Text:\n")
        print(summary)

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
