import speech_recognition as sr
import os
import pyttsx3
import speaker
import listener

import speaker
import listener
import os
import subprocess

def main():
    print("--- Система Сієста запускається ---")
    try:
        speaker.speak("Систему активовано. Я вас слухаю.")
    except Exception as e:
        print(f"Помилка динаміка: {e}")
    
    while True:
        command = listener.listen() 
        
        if not command:
            continue 

        print(f"Оброблена команда: {command}")

        if "сієста" in command:
            if "привіт" in command:
                speaker.speak("Привіт-привіт! Чим можу допомогти?")
                
            elif "відкрий google" in command or "браузер" in command:
                speaker.speak("Відкриваю браузер")
                subprocess.Popen(["xdg-open", "https://google.com"])
                
            elif "стоп" in command or "вийти" in command:
                speaker.speak("Бувай! Покличте, якщо буду потрібна.")
                break
                
            else:
                speaker.speak("Я почула своє ім'я, але не впевнена, що саме треба зробити.")

if __name__ == "__main__":
    # Важливо: в твоїм коді не вистачало закриваючої дужки main()
    main()

"""
engine = pyttsx3.init()

def start_siesta():
    # Тепер при виклику speak() буде працювати gTTS з файлу speaker.py
    speaker.speak("Систему активовано. Сієста готова до роботи, сер.")

if __name__ == "__main__":
    start_siesta()
    
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

if "відкрий браузер" in command:
    speak("Відкриваю браузер")
    os.system("xdg-open https://google.com")
elif "створи файл" in command:
    with open("new_file.txt", "w") as f:
        f.write("Привіт від Сієсти!")
    speak("Файл створено")
    """