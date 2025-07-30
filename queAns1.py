from transformers import pipeline
import PyPDF2

qaPipeline = pipeline("question-answering", model="deepset/minilm-uncased-squad2")

try:
    with open("insurance_policy.pdf", "rb") as pdfFile:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        fullText = ""
        for page in pdfReader.pages:
            fullText += page.extract_text()
except FileNotFoundError:
    print("The file 'insurance_policy.pdf' was not found.")
    exit()
except Exception as error:
    print(f"Error reading the PDF: {error}")
    exit()

while True:
    userQuestion = input("\nEnter your question about the policy (or type 'exit' to quit): ")
    if userQuestion.lower() in ["exit", "quit"]:
        print("Exiting the program.")
        break
    try:
        result = qaPipeline(question=userQuestion, context=fullText)
        print("Answer:", result['answer'])
    except Exception as error:
        print("Error during question answering:", error)
