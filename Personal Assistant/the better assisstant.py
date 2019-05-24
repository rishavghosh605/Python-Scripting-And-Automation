import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time

# The engine which we will use for the computer to talk back to us
engine = pyttsx3.init('sapi5')

# The wolphram client id to use wolframalpha 
client = wolframalpha.Client('7QJ4YH-T5RP7VR292')

# We can use any random voice from the ones that our PC has
voices = engine.getProperty('voices')
print("voices",voices)
engine.setProperty('voice', voices[len(voices)-1].id)

# The module that lets us hear the text to speech translation by the computer
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

# The module that uses the current time to greet the client appropriately
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')


def formality():
    greetMe()
    speak('I am your digital assistant!')
    speak('What is your name?')
    user=myCommand()
    speak('Do you want to give me a name?')
    choice=myCommand()
    if choice=="Yes":
        speak('What is my name {}:'.format(user))
        name=myCommand()
        return [user,name]
    return [user,"your Assisstant"]


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    except sr.RequestError:
            print('Hey, check if you have an internet connection')
            time.sleep(10) # To let the person check his internet connection while the script sleeps

    return query

def assisstant(names):
    query = myCommand();
    query = query.lower()
    okay='okay {}'.format(names[0])
    if 'open youtube' in query:
        speak(okay)
        webbrowser.open('www.youtube.com')

    elif 'open google' in query:
        speak(okay)
        webbrowser.open('www.google.co.in')

    elif 'open gmail' in query:
        speak(okay)
        webbrowser.open('www.gmail.com')

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(random.choice(stMsgs))

    elif 'email' in query:
        speak('Who is the recipient? ')
        recipient = myCommand()

        if 'me' in recipient:
            try:
                speak('What should I say? ')
                content = myCommand()
    
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login("Your_Username", 'Your_Password')
                server.sendmail('Your_Username', "Recipient_Username", content)
                server.close()
                speak(okay)
                speak('Email sent!')

            except:
                speak('Sorry Sir! I am unable to send your message at this moment!')


    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak(okay)
        speak('Bye and, have a good day.')
        sys.exit()
       
    elif 'hello' in query:
        speak('Hello {} this is {}. I am Listening'.format(names[0]))

    elif 'bye' in query:
        speak('Bye,{}'.format(names[0]))
        speak('have a good day.')
        sys.exit()
                                
    elif 'play music' in query:
        music_folder = Your_music_folder_path
        music = [music1, music2, music3, music4, music5]
        random_music = music_folder + random.choice(music) + '.mp3'
        os.system(random_music)
              
        speak('Okay, here is your music! Enjoy!')
        

    else:
        query = query
        speak('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                speak('Got it.')
                speak(results)
                
            except:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                speak(results)
    
        except:
            webbrowser.open('www.google.com')
    
    speak('Next Command! Sir!')

if __name__ == '__main__':

    names=formality()

    while True:
        assisstant(names)
    
        
