# Py_AI
Talk to your computer and have it do stuff for you!

In the main TT1.py file there a numerous different tasks that your Computer can do. It's designed to run on linux machines, with planned support for Windows machines further down the line.

# Files and Functions (Predefined)
### mods/extra.py 
#### introduction()
This is a quick introduction in the extra.py file. It's used to tell the user who the A.I is as well as it's function.
#### quote()
This function uses the forismatic.com API and tells you a randomly selected Quote.

### mods/ipSend.py
#### ipSend()
Gets your IP ADDRESS and tells you both your public and private IP. Then asks if you want both of them sent to you by email. (For Configuration of email, refer to sendMail.py)

### mods/listen.py
#### listen()
Initiates the microphone and runs google's speech recognition API against the captured input. Returns a string of the recognized speech. This is what is used to talk to your A.I.

### mods/say.py
#### say(Talk, TimeOfDay=None,slow=False)
Get's your A.I to start talking. The "Talk" parameter is used to tell the A.I what you want it to say. The "TimeOfDay" parameter allows for you to make responses dynamic based upon time of day. Finally, the "slow" parameter allows for you to define if you want the A.I to say something slow as opposed to normal speed. This can be set to either Boolean.

### mods/sendMail.py
#### sendMail(thelist)
Currently sends mail pertaining to a list given off from the ipSend() function. Here, you can customize your email address as well as message formatting.

### mods/sqlStart.py
#### databaseSSH()
Used to ssh into other machines. Reads from the CSV file in the "data" folder and copies each IP entry to a database file that's also written to the "data" folder. The CSV only is used to append entries. If you want to remove an entry, you have to delete the database file. Returns a list of each entry in the database.

### mods/ssh.py
#### ssh(available_SSH)
Reads from the list that was returned by the databaseSSH() function and tells you the IP addresses you have available, to ssh into. Then asks which from the list you would want to SSH into.

### TT1.py (Main File)
#### internetOn() 
Checks to see if the Internet is working on your machine. If it is, you'll use the Google speech recognizer, which is much more accurate and faster than the PocketSphinx speech recognizer. It returns True or False. If it returns false, you're gonna be using the PocketSphinx recognizer.

#### talk()
Initializes the internetOn() function and stores it's value. If that value is true, you're gonna use the Google recognizer. If the value is false, you're going to get an error, telling you there is no internet connection.

#### speechGoogle()
Sits and waits for you to say the keyword("Hey Tina", or "Hello Tina").Then it moves on to the next function, which asks you to give it instructions based on whatever you have defined.

#### Google()
Uses the google speech recognition API and this is where you tell your A.I what you want to do. This is the glue that keeps each piece working together. If what you say has a certain keyword, then the corresponding function will run.

# Default Keywords
#### TEMPERATURE -- temp()
#### ADDRESS -- ipSend()
#### SSH -- ssh(available_SSH)
#### QUOTE -- quote()
#### "TEST" and "HAT" -- hatTest()
#### "MY NAME" or "INTRODUCE" -- introduction()

# Future
All of this is editable. If you would like further additions, newer features, or have any ideas, feel free to email me at gravim3tric@outlook.com. Alternatively, you can download the source code yourself, and add more to the "mods" folder where each function is written, then update the main TT1.py file so you can assign that function a keyword.
