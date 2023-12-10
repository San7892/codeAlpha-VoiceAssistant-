import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        command = recognizer.recognize_wit(audio, key="YOUR_WIT_AI_API_KEY").lower()
        print(f"You said: {command}")
        return command

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return None

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "what is your name" in command:
        speak("I am your custom voice assistant.")
    elif "goodbye" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your custom voice assistant.")
    
    while True:
        command = listen()
        if command:
            process_command(command)
