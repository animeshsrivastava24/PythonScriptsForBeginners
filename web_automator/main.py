from google_auto import google_automator
from youtube_auto import youtube_automator
from facebook_auto import facebook_automator
import pyfiglet
import pyttsx3
import subprocess
import os
subprocess.call('clear')
banner_name="AutoPY"
print(pyfiglet.figlet_format(banner_name))
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("rate", 170)
def main():
    while True:
        print("1.Google Search")
        print("2.Youtube Search")
        print("3.Facebook Login")
        choice=str(input('Enter your choice : '))
        if choice=='1':
            engine.say("Starting Google Search")
            engine.runAndWait()
            subprocess.call('clear')
            google_automator()
        elif choice=='2':
            engine.say("Starting Youtube Search")
            engine.runAndWait()
            subprocess.call('clear')
            youtube_automator()
        elif choice=='3':
            engine.say("Starting Facebook Login")
            engine.runAndWait()
            subprocess.call('clear')
            facebook_automator()
        else:
            engine.say("Invalid option chosen")
            engine.runAndWait()
            print("Invalid Choice")

engine.say("Welcome to the python automator") 
engine.runAndWait()           
main()
