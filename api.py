from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot import get_response

app = FastAPI()

# Allow browser to talk to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chat")
def chat(message: str):
    response = get_response(message)
    return {"response": response}
