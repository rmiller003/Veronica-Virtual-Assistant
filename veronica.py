# This is a Speech recognition Virtual assistant application using Google AI Voice modules
# Written by Robert Miller in Python 3.8


import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import pywhatkit
import pyautogui
import webbrowser
import playsound
import pytime
import json
import requests
from urllib.request import urlopen

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('Hello, my name is veronica')
audio_file = '95.mp3'
playsound.playsound(audio_file)
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            audio_file = 'science.mp3'
            playsound.playsound(audio_file)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'veronica' in command:
            command = command.replace('veronica', '')
            print(command)

    except:
        pass
    return command

def sleep():
    sleep = 1

def time_():
    Time=datetime.datetime.now().strftime('%I:%M %p')
    talk("The current time is")
    talk(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    talk("The current date is")
    talk(month)
    talk(date)
    talk(year)

def wishme():
    talk("Welcome back Robert")
    time_()
    date()

# Greetings

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        talk("Good Morning Robert")
    elif hour>=12 and hour<18:
        talk("Good Afternoon Robert")
    elif hour>=18 and hour<24:
        talk("Good Evening Robert")
    else:
        talk("Good Night Robert")

    talk("Veronica at your service. Please tell me how I can help you today?")

wishme()

def run_veronica():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'date' in command:
        talk('The Current date is  ')
        date()

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'search' in command:
        search = command.replace('search', '')
        talk('searching ' + '')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('Here is what I found' + search)

    elif 'where' in command:
        location = command.replace('where is', '')
        talk('searching ' + '')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        talk('Here is the location for' + location)

    elif 'who do you answer to' in command:
        talk('Robert Miller, he is my creator and my allegiance is to him and only him')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'tell me your primary function' in command:
        talk('My name is Veronica, I am a virtual assistant designed to answer your queries as best as I can')

    elif 'how do you feel' in command:
        talk('I am operating at peak efficiency and look forward to to answering your queries as best as I can')

    elif 'switch the window' in command:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pytime.sleep(1)
        pyautogui.keyUp("alt")

    elif 'news' in command:
        jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&catagory=technology&apiKey=3b428458d28f453eabf5b58a7f0a3ed9")
        data = json.load(jsonObj)
        i = 1

        talk('Here are the latest headlines from the Tech Industry')
        print('=============LATEST HEADLINES============='+'\n')
        for item in data['articles']:
            print(str(i)+'. '+item['title']+'\n')
            print(item['description']+'\n')
            talk(item['title'])
            i += 1

        # except Exception as e:
        #         print(str(e))

    elif 'shut down' in command:
        talk('Acknowledged, Im shutting down the system, Goodbuy')
        audio_file = 'shutdown.mp3'
        playsound.playsound(audio_file)
        exit()

    else:
        talk('Please say the command again.')


while True:
    run_veronica()

