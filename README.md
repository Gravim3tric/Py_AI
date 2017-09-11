# Py_AI
Talk to your computer and have it do stuff for you!

In the main TT1.py file there a numerous different tasks that your Computer can do. It's designed to run on linux machines, with planned support for Windows machines further down the line.

# Functions (Predefined)
### internetOn() 
Checks to see if the Internet is working on your machine. If it is, you'll use the Google speech recognizer, which is much more accurate and faster than the PocketSphinx speech recognizer. It returns True or False. If it returns false, you're gonna be using the PocketSphinx recognizer.

### talk()
Initializes the internetOn() function and stores it's value. If that value is true, you're gonna use the Google recognizer. If the value is false, you're gonna use the PocketSphinx recognizer.

### speechSphinx() and speechGoogle()
Both of these sit and wait for you to say the keyword("Hey Tina", or "Hello Tina").Then it moves on to the next function, which asks you to give it instructions based on whatever you have defined.
