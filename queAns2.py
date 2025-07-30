import os
import PyPDF2
from docx import Document
from transformers import pipeline

def extractTextFromFile(filePath):
    if filePath.lower().endswith('.pdf'):
        with open(filePath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            return text
    elif filePath.lower().endswith('.docx'):
        doc = Document(filePath)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif filePath.lower().endswith('.txt'):
        with open(filePath, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format")

def answerQuestions(documentText):
    qaPipeline = pipeline("question-answering", model="deepset/minilm-uncased-squad2")
    while True:
        userQuestion = input("Enter your question (or type 'quit' to exit): ")
        if userQuestion.lower() == 'quit':
            break
        result = qaPipeline(question=userQuestion, context=documentText)
        print("Answer:", result['answer'])

filePath = input("Enter the path to the sales policy document: ")
try:
    documentText = extractTextFromFile(filePath)
    if not documentText.strip():
        print("The document is empty.")
    else:
        answerQuestions(documentText)
except Exception as error:
    print("Error:", error)


