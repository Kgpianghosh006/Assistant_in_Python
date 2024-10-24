import speech_recognition as sr
import pyttsx3
from google.cloud import speech
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if c.lower().startswith('open'):
        website = c.lower().split(' ')[1]
        from bs4 import BeautifulSoup
        import requests
        response = requests.get(url=f'https://www.google.com/search?q={website}&ln=en')
        soup = BeautifulSoup(response.text, 'html.parser')
        speak(soup.text)


if __name__ == "__main__" :
    speak("Initializing JARVIS...")

    while True:
        r = sr.Recognizer()
        print("Listening...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            # Recognize the speech
            text = r.recognize_google(audio)
            print("Recognized speech: ", text)
            if text.lower() == "jarvis":
                speak("Jarvis activated")
            processCommand(text)
        except sr.RequestError as e:
            print("Error; {0}".format(e))