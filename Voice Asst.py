import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            # [span_5](start_span)Requirement: Recognize voice commands[span_5](end_span)
            query = recognizer.recognize_google(audio).lower()
            print(f"User said: {query}")
            return query
        except Exception:
            return "none"

def run_assistant():
    command = listen_command()
    
    # [span_6](start_span)Requirement: Responding to "Hello"[span_6](end_span)
    if 'hello' in command:
        speak("Hello! I am your Oasis Infobyte assistant. How can I help you?")
    
    # [span_7](start_span)Requirement: Telling the time[span_7](end_span)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")
    
    # [span_8](start_span)Requirement: Searching the web[span_8](end_span)
    elif 'search' in command:
        speak("What should I search for?")
        search_query = listen_command()
        if search_query != "none":
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query}")
    else:
        speak("I'm sorry, I don't know that command.")

if __name__ == "__main__":
    run_assistant()