#Python version 3.8.6
# pip install pyttsx3  
# pyttsx3 is a text-to-speech conversion library in Python.
import pyttsx3
# pip install speechRecognition 
# You can then use speech recognition in Python to convert the spoken words into text, make a query or give a reply. 
import speech_recognition as sr
# pip install wikipedia to search things on wikipedia
import wikipedia
# following are inbuilt modules
import webbrowser 
import datetime
import os
import random
# Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft. 
# It gives us some inbuit windows voices (male,female) which we can use in our speak function.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[1].id) # to check whose voice I am using (male or female)
# by changing index we can use different voices which microsoft provides.

# creating speak function to convert string into audio format.
def speak(audio):
    engine.say(audio)
    engine.runAndWait() # Blocks while processing all currently queued commands. Without this command, speech will not be audible to us.


def wishing():
    """ creating this function to wish the user"""
    hours = int(datetime.datetime.now().hour)  # taking 0 to 24 hours from datetime module and typecasting it

    if hours >= 0 and hours < 12:
        speak("Good Morning")

    elif hours >= 12 and hours < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("How may I help you boss")

# takeCommand will return a string which we can use to query in while loop 
# why search=False? in while loop we have added condition where we check is his query consist of search word if yes then we call takecommand() by passing text as an argument
# which will make search="your Text" which is equal to search=True then in takeCommand() function we added if condition where we ask user what he wants to search. then it will run the further code in
# takeCommand() function.
def takeCommand(search=False):
    """This takes microphone input from user and converts it into text/string"""
    '''creating an object r of a class Recoginzer, we create an object of a module using following syntax
    object_name=module_name.class_name() here as we have imported a speech_recognition module as sr that's why we 
    are using sr in place of module name'''

    # Initializing the object so that we can access all the methods of a class Recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:  # here the source is going to be our microphone
        if search:
            speak("What do you want to search for ?")
        print("Listening...")
        r.pause_threshold = 1 #It's in seconds
        audio = r.listen(source) 
    query = "" 
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language="en-US")  #Using google for voice recognition.
        print(f"You said: {query}\n")  # User query will be printed.

    except sr.UnknownValueError:  #These are some exception that needs to be handled.
        # Could you repeat what you just said for me, I didn't understand.... will be printed in case of improper voice
        print(" Could you repeat what you just said for me, I didn't understand....")
        # speak(" Could you repeat what you just said for me, I didn't understand....")
    except sr.RequestError:
        speak("Sorry my speech service is down")
    return query


if __name__ == "__main__":
    wishing()

    while True:
        query = takeCommand().lower() #converting query into lower case as I am making all if else statements in lowercase

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") # replacing wikipedia with empty string eg. python moudules wikipedia will be python modules.
            try:
                results = wikipedia.summary(query, sentences=2)
                speak(results)
                print(results)
            except wikipedia.DisambiguationError as e:
                s = random.choice(e.options)
                results = wikipedia.summary(query, sentences=2)
                speak(results)
                print(results)
         

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\Songs\\English'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(
                music_dir, songs[random.randint(0, len(songs)-1)]))

        elif 'play movie' in query:
            movie_dir = 'E:\\Hollywood\\Marvel & DC\\Marvel\\Avengers All Parts'
            movie = os.listdir(movie_dir)
            os.startfile(os.path.join(
                movie_dir, movie[random.randint(0, len(movie)-1)])) # This will play any random movie

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\maxvh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "what is your name" in query:
            speak("My name is Alfred")

        elif "search" in query:
            search = takeCommand("What do you want to search for?")
            if search:
                url = 'https://google.com/search?q='+search
                webbrowser.open(url)
        elif "exit" in query:
            speak("sayonara")
            exit()
