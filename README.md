# 🤖 Nikith AI Chatbot

A simple AI chatbot built using **Python, Machine Learning, and FastAPI**, capable of responding to user queries using **TF-IDF similarity and cosine similarity** on a custom dataset.

This project demonstrates how an AI chatbot can be **built from scratch and deployed on AWS EC2** without using any external AI APIs.

---

## 🌐 Live Demo

Try the chatbot here:

http://3.110.157.77:8000

⚠️ This is a basic demo chatbot and may not answer every question correctly.

---

##  Features


* Conversational chatbot interface
* TF-IDF similarity based response matching
* Custom dataset question-answer system
* Memory feature (remembers user's name)
* Web based chat interface
* Cloud deployment using AWS EC2
* No external APIs used

---

##  How It Works

The chatbot uses a **TF-IDF vectorization model** to convert text into numerical vectors.

When a user sends a message:

1. The message is converted into a TF-IDF vector
2. Cosine similarity is calculated between the user message and dataset questions
3. The most similar question is selected
4. The corresponding answer is returned

If similarity is low, the chatbot returns a fallback response.

---

##  Tech Stack

**Backend**

* Python
* FastAPI
* Scikit-learn

**Machine Learning**

* TF-IDF Vectorizer
* Cosine Similarity

**Frontend**

* HTML
* CSS
* JavaScript

**Deployment**

* AWS EC2 (Ubuntu Server)

---

## 📂 Project Structure

```
ai-chatbot-aws
│
├── chatbot.py
├── chatbot_dataset.csv
├── index.html
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/Srinikith4/ai-chatbot-aws.git
```

Navigate into the project folder:

```
cd ai-chatbot-aws
```

Install dependencies:

```
pip install fastapi uvicorn scikit-learn
```

Run the server:

```
python3 -m uvicorn chatbot:app --host 0.0.0.0 --port 8000
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## ☁️ AWS Deployment

The chatbot is deployed on an **AWS EC2 Ubuntu instance**.

Deployment steps:

1. Launch EC2 instance (t3.micro)
2. Install Python and required libraries
3. Upload project files
4. Run FastAPI server using Uvicorn
5. Configure security group to allow port **8000**

Live deployment:

```
http://3.110.157.77:8000
```

---

##  Example Questions

Try asking the chatbot:

```
hi
what is python
what is machine learning
who created you
my name is Nikith
what is my name
```

---

## ⚠️ Limitations

* The chatbot only answers questions from its dataset
* It does not generate responses using large language models
* Some questions may not produce accurate responses

This project is intended as a **learning demonstration of ML-based chatbots and cloud deployment**.

---

##  Author

**Nikith**

Built as a project to explore:

* Machine Learning basics
* Backend API development
* Cloud deployment with AWS

---

## ⭐ Future Improvements

* Larger training dataset
* Improved NLP processing
* Conversation history
* Docker deployment
* Authentication and logging

## 📸 Preview

   
   

<img width="1919" height="870" alt="demo screenshot" src="https://github.com/user-attachments/assets/dfffc049-3d1c-46df-b99c-01c6a9337fcd" />

