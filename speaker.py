import pyttsx3

def initialize_engine():
    """Налаштовує двигун синтезу мовлення."""
    engine = pyttsx3.init()
    
    # Налаштування швидкості мовлення (за замовчуванням 200, краще 170-180)
    engine.setProperty('rate', 170)
    
    # Налаштування гучності (0.0 до 1.0)
    engine.setProperty('volume', 1.0)
    
    return engine

def speak(text):
    """Функція, яка змушує асистента говорити."""
    engine = initialize_engine()
    
    # Вибір голосу (опціонально)
    # В Linux espeak має специфічні голоси, за замовчуванням вибере системний
    voices = engine.getProperty('voices')
    
    # Спробуємо знайти український голос, якщо він встановлений в системі
    for voice in voices:
        if "ukrainian" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
            
    print(f"Сієста: {text}")
    engine.say(text)
    engine.runAndWait()

# Цей блок спрацює тільки якщо ти запустиш цей файл напряму
if __name__ == "__main__":
    speak("Привіт! Я твій голосовий помічник. Система готова до роботи.")