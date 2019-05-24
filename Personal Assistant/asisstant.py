#gtts is google text to speech
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import smtplib
import os
from webbrowser_connector import webbrowser

#template webbrowser.get('chrome').open_new_tab(urL)
# this does not work so I used pyttsx3 for my next version
def talkToMe(audio):
    print(audio)
    tts=gTTS(text=audio,lang='en')
    tts.save('audio.mp3')# to save th audio file
    os.system('mpg123 audio.mp3')#we use a command line audio executor called mpg123 we install it in oython using pip as usual

#listen for commands

def myCommand():

    r=sr.Recognizer()#This atrribute will capture our speech that it recieves from our mic
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold=1#Gives a bit of time before it starts listening to the next command
        r.adjust_for_ambient_noise(source,duration=1)#Adjusts the energy threshold dynamically using audio from ``source`` (an ``AudioSource`` instance) to account for ambient noise.
                           #Intended to calibrate the energy threshold with the ambient energy level. Should be used on periods of audio without speech - will stop early if any speech is detected.
                            #The ``duration`` parameter is the maximum number of seconds that it will dynamically adjust the threshold for before returning. This value should be at least 0.5 in order
                            #to get a representative sample of the ambient noise.
        audio = r.listen(source)

        try:
            command=r.recognize_google(audio)#erforms speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
            print('You said: '+command+'/n')
            return command

        #loop back if we capture some speech that is unreconizable or some command
        #so we continue to loop back unitl we find recognizable speech

        except sr.UnknownValueError:
            print('Honey, speak more clearly')
        except sr.RequestError:
            print('Hey, check if you have an internet connection')
            
            

def assistant(command):
    
    if command != None:
        print(type(command),"+",command)
        
        if 'open Reddit python' in command:
            url='https://www.reddit.com/r/python'
            webbrowser.get('chrome').open_new_tab(url)#Opens the given url

        if 'what\'s up' in command:
            talkToMe('Chilling bro')

        if 'email' in command:
            talkToMe('Who is the recipient?')
            recipient=myCommand()

while True:
    assistant(myCommand())
            
