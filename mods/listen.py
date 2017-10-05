#!/usr/bin/env python3
import speech_recognition as sr
from mods.say import say
# get audio from the microphone

r = sr.Recognizer()
def listen():
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Speak:")
            audio = r.listen(source)
        try:
            print("You said " + r.recognize_google(audio).upper())
            return r.recognize_google(audio).upper()
        except sr.UnknownValueError:
            print("Could not understand audio")
            say("NOTHING")
        except sr.RequestError as e:
            say("NOTHING")
            print("Could not request results; {0}".format(e))
