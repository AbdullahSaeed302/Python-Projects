import requests
import json
import pyttsx3
import time

print("TempTracker 3.4 ••• Made by Abdullah >>>\n")
engine = pyttsx3.init()

engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def weather_finder():
    try:
        speak("Enter the name of the city")
        city_name = input("Enter the name of the city: ")

        url = f"http://api.weatherapi.com/v1/current.json?key=a8ed5b62996c46dc94685332241512&q={city_name}"

        request = requests.get(url)

        wdic = json.loads(request.text)

        dic_weather = wdic['current']['temp_c']

        print(f"\nChecking weather in {city_name}...\n")
        time.sleep(2)
        print(f"The current weather in '{city_name}' is {dic_weather} °C.")
        speak(f"The current weather in '{city_name}' is {dic_weather} °C.")

    except:
        print("Please enter a right city name!")
        speak("Please enter a right city name!")
        
while True:
    weather_finder()
    ask = input("\nWanna search again? (y/n): ")
    if ask != 'y':
        print("Thank you for using TempTracker!")
        speak("Thank you for using TempTracker!")
        break
