import csv
import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = []
answers = []

# memory storage
memory = {}

# Load dataset
with open("chatbot_dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 2:
            questions.append(row[0].lower())
            answers.append(row[1])

# Train vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)


def get_response(message):

    message = message.lower()

    #  MEMORY FEATURE 

    # detect name
    name_match = re.search(r"(my name is|i am|i'm|im)\s+([a-zA-Z]+)", message)
    if name_match:
        name = name_match.group(2)
        memory["name"] = name
        return f"Nice to meet you {name}!"

    if "what is my name" in message:
        if "name" in memory:
            return f"Your name is {memory['name']}."
        else:
            return "I don't know your name yet."

    # SMART DATASET MATCHING 

    msg_vector = vectorizer.transform([message])
    similarity = cosine_similarity(msg_vector, X)

    index = similarity.argmax()
    score = similarity[0][index]

    if score < 0.3:
        return random.choice([
            "I didn't understand that.",
            "Can you ask something else?",
            "Interesting... tell me more.",
            "I'm not sure about that."
        ])

    return answers[index]
