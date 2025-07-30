import os
import email
import extract_msg
from email import policy
from email.parser import BytesParser
from transformers import pipeline

def extractEmailText(filePath):
    if filePath.lower().endswith('.eml'):
        with open(filePath, 'rb') as file:
            msg = BytesParser(policy=policy.default).parse(file)
            subject = msg['subject'] or ''
            body = msg.get_body(preferencelist=('plain'))
            bodyText = body.get_content() if body else ''
            return f"Subject: {subject}\n\n{bodyText}"
    elif filePath.lower().endswith('.msg'):
        msg = extract_msg.Message(filePath)
        subject = msg.subject or ''
        bodyText = msg.body or ''
        return f"Subject: {subject}\n\n{bodyText}"
    else:
        raise ValueError("Unsupported file format")

def answerQuestions(emailText):
    qaPipeline = pipeline("question-answering", model="deepset/minilm-uncased-squad2")
    print("\nExtracted Email Content:\n")
    print(emailText)
    while True:
        userQuestion = input("\nAsk a question about this email (or type 'quit' to exit): ")
        if userQuestion.lower() == 'quit':
            break
        result = qaPipeline(question=userQuestion, context=emailText)
        print("Answer:", result['answer'])

filePath = input("Enter the path to the email file (.eml or .msg): ")
try:
    emailText = extractEmailText(filePath)
    if not emailText.strip():
        print("The email content is empty.")
    else:
        answerQuestions(emailText)
except Exception as error:
    print("Error:", error)
