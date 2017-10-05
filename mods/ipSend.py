from mods.sendMail import sendMail
import netifaces as ni
import requests
import json
from mods.say import say
from mods.listen import listen

def ipSend(): #Tells the IP Address of the Raspberry PI
    IPADDRESS = ni.ifaddresses("wlp3s0")[ni.AF_INET][0]['addr'] #Tells Current IP

    PUB_IP = requests.get("http://jsonip.com")
    PUB_IP = PUB_IP.json()["ip"]

    print(PUB_IP)
    say("The IP Address is {0}".format(IPADDRESS))

    say("And The Public IP Address is {0}".format(PUB_IP), slow=True)


    while True:
        say("EMAIL")
        try:
            recognized_Audio = listen()
            if "YES" in recognized_Audio:
                Combined_IP = [IPADDRESS, PUB_IP]
                sendMail(Combined_IP)
                print(Combined_IP)
                say("DONE")
                break
            if "NO" in recognized_Audio:
                say("DONE")
                break
        except Exception as e:
            say("NOTHING")
            continue
