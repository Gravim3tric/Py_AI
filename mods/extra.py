from mods.say import say
import requests
import json

def introduction(): #Just An Introduction
    say("Hello")
    say(""" My name is Tina.
    I was built in 2017 to be an artificial intelligence that's sole purpose
    is to make your life easier.""")

def quote(): #Get Quotes : Add option to get another
    while True:
        try:
            url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
            req = requests.get(url)
            req = req.json()
            quote = req["quoteText"]
            print(quote)
            say(quote)
            say("DONE")
            break

        except Exception as e:
            say("ERROR")
            print(e)
