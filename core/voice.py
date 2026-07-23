import speech_recognition as sr

from core.tts import PiperTTS


class Voice:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.tts = PiperTTS()

    def listen(self):

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"\nYou : {text}")

            return text

        except Exception:

            print("Sorry, I didn't catch that.")

            return ""

    def speak(self, text):

        print(f"\nEcho : {text}")

        self.tts.speak(text)