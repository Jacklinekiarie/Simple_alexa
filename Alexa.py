import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening... ')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command= command.lower()
            if 'alexa' in command:
                command= command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing song' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H : %M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('Who is ', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif ' give me a date' in command:
        talk('sorry,i do not go for dates but i can make you happy ')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say that command again')

while True:
    run_alexa()