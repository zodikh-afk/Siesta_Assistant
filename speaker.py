import os
from elevenlabs.client import ElevenLabs

# Ініціалізація клієнта
client = ElevenLabs(
    api_key="sk_e0f3182818b7efae5aace0926793f976bb5ce9b7ba441130"
)

def speak(text):
    print(f"Сієста: {text}")
    
    try:
        audio_generator = client.text_to_speech.convert(
            text=text,
            voice_id="EXAVITQu4vr4xnSDxMaL", # ID голосу Sarah
            model_id="eleven_multilingual_v2"
        )
        
        # Зберігаємо аудіо у файл
        filename = "siesta_voice.mp3"
        with open(filename, "wb") as f:
            for chunk in audio_generator:
                f.write(chunk)
        
        # Відтворення через mpg123
        # Додаємо 2>/dev/null, щоб прибрати помилки ALSA з екрана
        os.system(f"mpg123 -q {filename} 2>/dev/null")
        
        if os.path.exists(filename):
            os.remove(filename)
            
    except Exception as e:
        print(f"Помилка ElevenLabs: {e}")

if __name__ == "__main__":
    speak("Тепер я використовую оновлений метод генерації. Все має працювати!")