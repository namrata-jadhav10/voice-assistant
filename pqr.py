import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

API_KEY = 'b7d06ec7bcc681bcef0b8e6e781d0472'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    


def weather_info():
    city = 'Solapur'  # Replace with your city name
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}"

    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data.get("cod") != "404":
        try:
            weather_description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']

            speak(f"The weather in {city} is {weather_description}. The temperature is {temperature} Kelvin.")
        except KeyError:
            speak("Weather information not available for this city.")
    else:
        speak("City not found.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query


def create_gui():
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("500x500")
    root.configure(bg='lightblue')

    label = tk.Label(root, text="Welcome to Voice Assistant", font=('Arial', 20), bg='lightblue')
    label.pack(pady=20)

    description_label = tk.Label(root, text="Voice Assistant Description:", font=('Arial', 12), bg='lightblue')
    description_label.pack()

    description_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    description_area.pack()

    description_text = (
        "This Voice Assistant can perform various tasks:\n"
        "- Open YouTube and Google\n"
        "- Play music\n"
        "- Provide the current time\n"
        "- Check Weather\n"
        "- Respond to general queries\n"
        
    )

    description_area.insert(tk.INSERT, description_text)
    description_area.configure(state='disabled')

    button_frame = tk.Frame(root, bg='lightblue')
    button_frame.pack(pady=20)

    start_button = tk.Button(button_frame, text="Start Assistant", command=start_assistant, font=('Arial', 14), bg='green', fg='white')
    start_button.grid(row=0, column=0, padx=10, pady=10)

    weather_button = tk.Button(button_frame, text="Check Weather", command=weather_info, font=('Arial', 14), bg='blue', fg='white')
    weather_button.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()

def start_assistant():
    speak("I'm ready to assist you.")

    while True:
        query = takeCommand().lower()

        

        if 'open youtube' in query:
            speak("Here you go to Youtube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            music_file = r'C:\Users\kolha.SHRADDHA\Downloads\vandemataramflutebyrajeshcherthalaringtone-43151.mp3'
            os.startfile(music_file)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'exit' in query:
            speak("Thanks for using the assistant.")
            break

        elif "how are you" in query:
            speak("I am fine, Thank you.")

        elif "who made you" in query:
            speak("I have been created by shraddha, namrata, and vidya.")

        elif 'joke' in query:
            speak("Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!")
        elif 'your work' in query:
            speak("I'm here to assist you with various tasks such as providing information, playing music and more.")

        elif 'when were you created' in query:
            speak("I was created on October 25th, 2023.")

        else:
            speak("I don't have an answer for that. Please provide more specific commands.")




if __name__ == '__main__':
    create_gui()
