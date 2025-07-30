#models: facebook/bart-large-cnn | t5-base | google/pegasus-xsum
from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-xsum")

claimLetter = """
I am writing to report a car accident that occurred on July 20, 2025, at approximately 3:45 PM at the intersection of 5th Avenue and Main Street.
While I was driving within the speed limit and following all traffic rules, another vehicle ran a red light and collided with the rear side of my car.
My car sustained significant damage to the rear bumper and left tail light. The police were notified immediately, and a report was filed under case number #56789.
I have attached the photos of the damage, a copy of the police report, and repair estimates from an authorized workshop.
I would appreciate your prompt assistance in processing my claim and reimbursing the repair costs as per the policy agreement.
"""

summary = summarizer(claimLetter, max_length=120, min_length=30, do_sample=False)

print("Summary:\n", summary[0]['summary_text'])
