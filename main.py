import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слухаю вас...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="uk-UA")
        return query.lower()
    except:
        return ""

command = listen_command()

if "відкрий гугл" in command:
    speak("Відкриваю браузер")
    webbrowser.open("https://google.com")
elif "створи файл" in command:
    with open("new_file.txt", "w") as f:
        f.write("Привіт від Сієсти!")
    speak("Файл створено")