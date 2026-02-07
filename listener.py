import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Адаптація під шум у кімнаті
        r.adjust_for_ambient_noise(source, duration=1)
        print("Слухаю (Сієста)...")
        audio = r.listen(source)

    try:
        # Використовуємо Google для розпізнавання української
        query = r.recognize_google(audio, language="uk-UA")
        print(f"Ви сказали: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return "" # Якщо нічого не зрозумів
    except sr.RequestError:
        print("Помилка сервісу розпізнавання")
        return ""