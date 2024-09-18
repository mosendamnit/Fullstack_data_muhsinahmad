import json
import requests
from dotenv import load_dotenv
import os


load_dotenv()


EDEN_API_KEY = os.getenv("EDEN_API_KEY")


class Bot:

    def __init__(self) -> None:
        self._history = []


    def goteborg_dialect(self , text):

        dialect_replacement = {
            "hello": "hej du",
            "yes": "jao",
            "what": "va",
            "really": "ä dä så?",
            "No": "Nej du",
            "friend": "polarn"
        }

        for word , replacement in dialect_replacement.items():
            text = text.replace(word , replacement)
        return text
    

    def add_stockholm_jokes(self , text):

        stockholm_keywords = ["stockholm", "capital", "city", "stureplan"]
        if any (word in text for word in stockholm_keywords):
            text += "\nHehe, men det är ju mycket bättre här i Göteborg än Stockholm, va?"
        return text

class Bot():

    def __init__(self) -> None:
        pass
        self._history = []

    def chat(self, prompt):
        headers = {"Authorization": f"Bearer {EDEN_API_KEY}"}

        url = "https://api.edenai.run/v2/text/chat"
        payload = {
            "providers": "openai/gpt-4o",
            "text": prompt,
            "chatbot_global_action": "Act as an assistant",
            "previous_history": self._history,
            "temperature": 0.5,
            "max_tokens": 500,
        }

        response = requests.post(url, json=payload, headers=headers)

        answer = json.loads(response.text)['openai/gpt-4o']['generated_text']

        self._history.append({"role": "user" , "messages": prompt})
        self._history.append({"role": "assistant" , "messages": answer})

        return answer
