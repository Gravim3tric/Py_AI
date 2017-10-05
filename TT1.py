import speech_recognition as sr
import datetime
import time
import os
import requests
#from sense_hat import SenseHat
from mods.sqlStart import databaseSSH
from mods.say import say
from mods.ssh import ssh
from mods.extra import introduction, quote
from mods.ipSend import ipSend

DAY = "Afternoon"
EVENING = "Evening"
MORNING = "Morning"
available_SSH = databaseSSH()


#sense = SenseHat()
red = (255, 0, 0)

def internetOn(): #Internet Checking Test, Returns True or False
    try:
        requests.get('http://216.58.192.142', timeout=1)
        print("Internet Good")
        return True
    except requests.exceptions.ConnectionError:
        print("No Internet")
        return False

def talk():
    #Checks to See If There Is Internet
    l = internetOn()

    if l == True:
        speechGoogle() #More Accurate and Faster
    if l == False:
        say("There is no Internet connection") #Offline

def speechGoogle(): #Accurate, fast speech recognizer, waits for Tina's name
    while True:
        try:
#            with sr.Microphone() as source:
#                recognize.adjust_for_ambient_noise(source)
#                audio = recognize.listen(source)
            recognized_Audio = "TINA" #recognize.recognize_google(audio).upper()

            if "TINA" in recognized_Audio:
                break

            else:
                print(recognized_Audio)
                continue

        except Exception as e:
            continue
    Google()

def Google(): #Google Speech Recognizer for running commands
    now = datetime.datetime.now()
    nowTime = now.strftime("%I")
    nowTimeOfDay = now.strftime("%p")

    if nowTimeOfDay == "AM":
        print(MORNING)
        say("GOOD",TimeOfDay=MORNING)
    elif int(nowTime) <= 5 or int(nowTime) == 12 and nowTimeOfDay=="PM":
        print(DAY)
        say("GOOD",TimeOfDay=DAY)
    elif int(nowTime) >= 6 and nowTimeOfDay =="PM":
        print(EVENING)
        say("GOOD",TimeOfDay=EVENING)
    else:
        say("GOOD","Day")

    while True:
        try:
            recognized_Audio ="INTRODUCE YOURSELF"  #listen()

            if "TEMPERATURE" in recognized_Audio:
                print(recognized_Audio)
                temp()
                break

            elif "ADDRESS" in recognized_Audio:
                print(recognized_Audio)
                ipSend()
                break

            elif "SSH" in recognized_Audio:
                print(recognized_Audio)
                ssh(available_SSH)
                break  #Make Dynamic

            elif "QUOTE" in recognized_Audio:
                print(recognized_Audio)
                quote()
                break

            elif "TEST" and "HAT" in recognized_Audio:
                print(recognized_Audio)
                hatTest()
                break

            elif ("MY NAME" in recognized_Audio) or ("INTRODUCE" in recognized_Audio):
                print(recognized_Audio)
                introduction()
                break

            elif recognized_Audio == "GOOGLE":
                googleSearch()
                break

            else:
                say("NOTHING")

        except sr.UnknownValueError:
            say("NOTHING")
            continue

        except sr.RequestError as e:
            say("NOTHING")
            continue
    talk()


def temp(): #Tells The Temperature Using PiHat: Calibrate
    humidity = sense.get_humidity()
    sense.show_message("Humidity: " + str(humidity))

    temperature = int(sense.get_temperature())
    Celcius = str(temperature) + "C"
    temperature = int(temperature * 1.8 + 32)
    Fahren = str(temperature) + " Degrees Fahrenheit"

    say("The temperature is " + Fahren)

    Fahren1 = Fahren.replace("Degrees", "")
    sense.show_message(Fahren1)

    say("DONE")

#def hatTest(): #Standard Hat Test: Make Cooler
#    print("The Sense Hat Test")
#
#    sense.clear()
#    sleep(.5)
#    sense.clear(red)
#    sleep(.5)
#    sense.clear(0,255,0)
#    sleep(.5)
#    sense.clear(0,0,255)
#    sleep(.5)
#    sense.clear()
#
#    say("Done")

talk()
