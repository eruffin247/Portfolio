import requests #requests allows user to send http/s requests.

OLLAMA_URL = "http://localhost:11434/api/generate" #this is the local API where Ollama runs.

def ask_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model" : "ollama",
            "prompt" : prompt,
            "stream" : False
        }
    )
