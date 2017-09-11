import speech_recognition as sr
from gtts import gTTS
import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import netifaces as ni
import smtplib
from sense_hat import SenseHat
import json
import paramiko


sshlist = {"RASPBERRY 1":["INSERT IP","INSERT PASSWORD","INSERT USERNAME"], #SSH List for different machines, configure to your liking
"RASPBERRY 2":["IP2","PASSWORD2","USERNAME2"],
}

sense = SenseHat()
red = (255, 0, 0)

try:
    IPADDRESS = ni.ifaddresses("wlan0")[ni.AF_INET][0]['addr'] #Tells Current IP
except:
    None

recognize = sr.Recognizer() #Starts the Speech Recognizer

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
        speechSphinx() #Offline

def speechSphinx(): #The Less Accurate Speech Recognizer: Gonna Get Rid of It
    while True:
        try:
            with sr.Microphone(device_index=2,sample_rate= 16000) as source:
                recognize.adjust_for_ambient_noise(source)
                audio = recognize.listen(source)
                recognized_Audio = recognize.recognize_sphinx(audio).upper()

            if recognized_Audio =="HELLO TINA":
                break
            else:
                print(recognized_Audio)
                continue
        except Exception as e:
            continue
    Sphinx()

def speechGoogle(): #Accurate, fast speech recognizer, waits for Tina's name
    while True:
        try:
            with sr.Microphone(device_index=2, sample_rate= 16000) as source:
                recognize.adjust_for_ambient_noise(source)
                audio = recognize.listen(source)
                recognized_Audio = recognize.recognize_google(audio).upper()

            if "TINA" in recognized_Audio:
                break

            else:
                print(recognized_Audio)
                continue

        except Exception as e:
            continue
    Google()

def sendmail(thelist): #Sends Emails Based on What's in List: Make it check for IP, add different email options
    me = "INSERT EMAIL SENDING ACCOUNT"
    you = "INSERT EMAIL DESTINATION"


    msg = MIMEMultipart()
    msg["From"] = me
    msg["to"] = you
    msg["Subject"] = "Your IP ADDRESSES"

    body = "Your Raspberry Pi's IP Address is: %s\nYour Raspberry Pi's Public IP is: %s" % (thelist[0],thelist[1])
    msg.attach(MIMEText(body, "plain"))
    print(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(me,"12345678")
    text = msg.as_string()
    server.sendmail(me,you,text)
    server.quit()

def talkBack(Talk): #Predefined Responses for cleaner code
    if Talk == "GOOD":
        tts = gTTS(text="Hello, How Can I Help You?", lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")

    elif Talk == "DONE":
        tts = gTTS(text="I'm Done", lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")

    elif Talk == "ERROR":
        tts = gTTS(text="There was an error, let's try that again.", lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")

    elif Talk == "EMAIL":
        tts = gTTS(text="Would you like me to email that to you?", lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")


    else:
        tts = gTTS(text="I could not understand you.", lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")

def Google(): #Google Speech Recognizer for running commands
    talkBack("GOOD")
    while True:
        with sr.Microphone(device_index=2,sample_rate= 16000) as source:
            recognize.adjust_for_ambient_noise(source)
            audio = recognize.listen(source)

        try:
            recognized_Audio = recognize.recognize_google(audio).upper()

            if "TEMPERATURE" in recognized_Audio:
                temp()
                break

            elif "ADDRESS" in recognized_Audio:
                print (recognized_Audio)
                ipSend()
                break

            elif "SSH" or "LOG IN" in recognized_Audio:
                ssh("SSH",address=sshlist["RASPBERRY 1"][0],password=sshlist["RASPBERRY 1"][1],username=sshlist["RASPBERRY 1"][2])
                break  #Make Dynamic

            elif "QUOTE" or "GIVE ME" in  recognized_Audio: #Runs ssh Function: Fix
                Quote()
                print("HIII")
                break

            elif "TEST" and "HAT" in recognized_Audio:
                hatTest()
                break

            elif "MY NAME" or "INTRODUCE" in recognized_Audio:
                introduction()
                break

            elif recognized_Audio == "GOOGLE":
                googleSearch()
                break

            else:
                talkBack("NOTHING")

        except sr.UnknownValueError:
            talkBack("NOTHING")
            continue

        except sr.RequestError as e:
            talkBack("NOTHING")
            continue
    talk()

def Sphinx():
    talkBack("GOOD")
    with sr.Microphone(device_index=2,sample_rate= 16000) as source:
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)

    while True:
        try:
            recognized_Audio = recognize.recognize_sphinx(audio).upper()

            if "TEMPERATURE" in recognized_Audio:
                temp()

            elif "IP" or "ADDRESSES" in recognized_Audio:
                ipSend()
                break

            elif "HAT" in recognized_Audio:
                hatTest()
                break

            elif recognized_Audio == "GOOGLE":
                googleSearch()
                break
            else:
                talkBack("NOTHING")
                continue

        except Exception as e:
            talkBack("NOTHING")
            continue
    talk()

def temp(): #Tells The Temperature Using PiHat: Calibrate  
    humidity = sense.get_humidity()
    sense.show_message("Humidity: " + str(humidity))

    temperature = int(sense.get_temperature())
    Celcius = str(temperature) + "C"
    temperature = int(temperature * 1.8 + 32)
    Fahren = str(temperature) + " Degrees Fahrenheit"

    tts = gTTS(text="The temperature is " + Fahren, lang="en") 
    tts.save("greet.mp3")
    os.system("mpg321 greet.mp3")

    Fahren1 = Fahren.replace("Degrees", "")
    sense.show_message(Fahren1)

    talkBack("DONE")

def hatTest(): #Standard Hat Test: Make Cooler
    print("The Sense Hat Test")
    
    sense.clear()
    sleep(.5)
    sense.clear(red)
    sleep(.5)
    sense.clear(0,255,0)
    sleep(.5)
    sense.clear(0,0,255)
    sleep(.5)
    sense.clear()    

    talkBack("Done")


def ipSend(): #Tells the IP Address of the Raspberry PI
    PUB_IP = requests.get("http://jsonip.com")
    PUB_IP = PUB_IP.json()["ip"]

    print(PUB_IP)
    tts = gTTS(text="The IP Address is {0}".format(IPADDRESS), lang="en", slow=True)
    tts.save("greet.mp3")
    os.system("mpg321 greet.mp3")

    tts = gTTS(text="And The Public IP Address is {0}".format(PUB_IP), lang="en", slow=True)
    tts.save("greet.mp3")
    os.system("mpg321 greet.mp3")

    while True:
        with sr.Microphone(device_index=2,sample_rate= 16000) as source:
            recognize.adjust_for_ambient_noise(source)
            talkBack("EMAIL")
            print("Say Stuff")
            audio = recognize.listen(source)
            try:
                recognized_Audio = recognize.recognize_google(audio).upper()
                if "YES" in recognized_Audio:
                    Combined_IP = [IPADDRESS, PUB_IP]
                    sendmail(Combined_IP)
                    print(Combined_IP)
                    break
                if "NO" in recognized_Audio:
                    break
            except Exception as e:
                talkBack("NOTHING")
                continue

    talkBack("DONE")

def introduction(): #Just An Introduction
    tts = gTTS(text="""Hello. My name is Tina. I was built in 2017 to be an artificial
    intelligence that's sole purpose is to make your life easier.""", lang="en")
    tts.save("greet.mp3")
    os.system("mpg321 greet.mp3")

def Quote(): #Get Quotes : Add option to get another
    while True:
        try:
            url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
            req = requests.get(url)
            req = req.json()
            quote = req["quoteText"]
            print(quote)
            tts = gTTS(text=quote, lang="en")
            tts.save("greet.mp3")
            os.system("mpg321 greet.mp3")
            talkBack("DONE")
            break
        except:
            talkBack("ERROR")

def ssh(protocol, address, password, username): #Clean Up: Find Better Method

    if protocol == "SSH":
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address, username=username, password=password)
        stdin,stdout,stderr = ssh.exec_command("ls")
        output = stdout.readlines()
        print(len(output))
        tts = gTTS(text="There are {0} entries in the Home Folder.".format(len(output)), lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")
        talkBack("DONE")
        break

except Exception as exp:
    talkBack("ERROR")
    talkBack("DONE")
#

def googleSearch():
    print("Google's a phrase")
    talkBack("DONE")

talk()
