import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language=os.getenv("GOOGLE_SPEECH_LANG"))
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()

if __name__ == "__main__":
    while True:
        query = listen()
        if 'exit' in query or 'goodbye' in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            # Add your bot's response logic here
            speak("I heard you say, " + query + ". Now, I will process your request.")