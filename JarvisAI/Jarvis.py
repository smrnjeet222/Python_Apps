import pyttsx3
import random
import os
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir!")
    elif hour > 12 and hour <= 17:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am Jarvis. How may I help U")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source, duration = 0.8)
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again pls...")
        return "NONE"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('testyoyo222@gmail.com', 'password')
    server.sendmail('testyoyo222@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            query = query.replace("search" , "")
            result = wikipedia.summary(query  , sentences=2 )
            result = result.replace("pronunciation" , "")
            speak('According to Wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")
        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")
        elif 'open geeksforgeeks' in query:
            webbrowser.open("https://www.geeksforgeeks.org/data-structures/")
        elif 'open drive' in query:
            webbrowser.open("https://drive.google.com")
        elif 'open spotify' in query:
            spotify = "C:\\Users\\simranjeet\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)
        elif 'open code' in query:
            code = "C:\\Users\\simranjeet\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)
        elif 'open photos' in query:
            folder = "D:\\Simranjeet\\Pictures\\Saved Pictures"
            photo = os.listdir(folder)
            # print(photo)
            ran = random.randint(0 ,40) 
            os.startfile(os.path.join(folder , photo[ran]))
        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print (Time)
            speak (f"Sir, The Time is {Time}")
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "smrnjeet222@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, email not send")  

