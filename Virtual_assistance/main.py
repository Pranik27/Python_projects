# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 03:27:07 2020

@author: PRANIKP

An intelligent Virtual assistant that can perform tasks or services for an 
individual based on commands or questions. 

Libraries used: speech_recognition, pyttsx3, pywhatkit, datetime, Wikipedia, pyjokes

"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyPDF2

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    talk("Hello Pranik, How can i help you?")
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'read' in command:
        book = open('OOP.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        
        speaker = pyttsx3.init()
        for num in range(pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
    
    
































