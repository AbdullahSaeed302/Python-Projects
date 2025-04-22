import speech_recognition as sr
import pyttsx3
import webbrowser
from musicLibrary import musicLibrary
from difflib import get_close_matches
from datetime import datetime
import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Setup voices and properties
voices = engine.getProperty('voices')
engine.setProperty('rate', 135)
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Use pyttsx3 to speak the text."""
    engine.say(text)
    engine.runAndWait()

def Jarvis_greetings():
    diff_greets = [
        "At your service sir!",
        "How can I assist you sir?",
        "Yes master!",
        "What can I do for you?",
        "I'm listening!"
    ]
    return diff_greets

def find_best_match(song_title, library_keys):
    """Find the closest match to the song title from the music library."""
    matches = get_close_matches(song_title, library_keys, n=1, cutoff=0.5)
    return matches[0] if matches else None

def get_time():
    """Return the current time."""
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    """Return the current date."""
    now = datetime.now()
    return now.strftime("%m-%d-%Y")

def greet():
    speak("Waalaiikumm Assaalaam!")

def love():
    speak("I love you too...")

def deactivate():
    speak("Jarvis Deactivated...")
    exit()

def tell_joke():
    """Return a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the computer go to the doctor? It had a virus!"
    ]
    return random.choice(jokes)

def open_website(url, site_name):
    """Open a website and provide feedback."""
    try:
        webbrowser.open(url)
        speak(f"Opening {site_name}.")
    except Exception as e:
        speak(f"Sorry, I couldn't open {site_name}. There was an error: {e}")

def play_song(song_title):
    """Play the song directly from the music library by opening the YouTube link."""
    closest_match = find_best_match(song_title, musicLibrary.keys())

    if closest_match:
        # Get the YouTube URL from the music library
        youtube_url = musicLibrary[closest_match]

        try:
            speak(f"Playing {closest_match} on YouTube...")
            webbrowser.open(youtube_url)  # Open the YouTube video directly
        except Exception as e:
            speak(f"Error playing {closest_match} on YouTube: {e}")
    else:
        speak(f"Sorry, I couldn't find {song_title} in your music library.")
        
def processCommand(text):
    """Process the command given by the user."""
    if text is None:
        return

    text = text.lower()

    if "open google" in text:
        open_website("https://google.com", "Google")
    elif "open youtube" in text:
        open_website("https://youtube.com", "YouTube")
    elif "open facebook" in text:
        open_website("https://facebook.com", "Facebook")
    elif "open instagram" in text:
        open_website("https://instagram.com", "Instagram")
    elif "open chat gpt" in text:
        open_website("https://chatgpt.com", "ChatGPT")
    elif "play song" in text:
        song_title = text.replace("play song", "").strip().lower()
        play_song(song_title)
    elif "time" in text:
        print(f"The current time is {get_time()}.")
        speak(f"The current time is {get_time()}.")
    elif "date" in text:
        print(f"Today's date is {get_date()}.")
        speak(f"Today's date is {get_date()}.")
    elif "tell me a joke" in text:
        joke = tell_joke()
        print(joke)
        speak(joke)
    elif "text to speech" in text:
        speak("Write what you want to be spoken!")
        user_input = input("Write what you want to be spoken: ")
        speak(user_input)
    elif "salam" in text:
        greet()
    elif "i love you" in text:
        love()
    elif "deactivate" in text:
        deactivate()
    else:
        speak("Sorry, I didn't understand that. Would you like to try again?")

def listen_for_command():
    """Listen for the user's command using speech recognition."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said. Could you please repeat that?")
        return None
    except sr.RequestError:
        speak("Sorry, there seems to be a problem with the speech recognition service. Please try again later.")
        return None
    except sr.WaitTimeoutError:
        speak("I'm waiting for you to speak, please try again.")
        return None
    except Exception as e:
        speak(f"An unexpected error occurred: {e}")
        return None

if __name__ == '__main__':
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing...")

        # Recognize speech using Google!
        word = listen_for_command()
        if word:
            if "jarvis" in word.lower():
                speak(random.choice(Jarvis_greetings()))
                command = listen_for_command()
                if command:
                    processCommand(command)
            elif "deactivate" in word.lower():
                speak("Jarvis Deactivated...")
                break