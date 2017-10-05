from gtts import gTTS
import os

def say(Talk,TimeOfDay=None, slow=False): #Responses for cleaner code
    if Talk == "GOOD":
        tts = gTTS(text="Good {0}, How Can I Help You?".format(TimeOfDay), lang="en")
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

    elif Talk == "NOTHING":
        tts = gTTS(text="I'm sorry, I could not understand you.", lang="en")
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")

    else:
        tts = gTTS(text=Talk, lang="en", slow=slow)
        tts.save("greet.mp3")
        os.system("mpg321 greet.mp3")
