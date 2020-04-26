import time
import datetime
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
C = 0


def speak(text):
    global C
    C += 1
    tts = gTTS(text=text, lang="en")
    filename = f'Voices/voice{C}.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <= 12:
        speak("Good Morning Sir!")
    elif hour > 12 and hour <= 17:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am Siri. How may I help U")


def get_audio():
    r = sr.Recognizer()
    print('Listening......')
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


if __name__ == '__main__':
    WishMe()
    while True:
        txt = get_audio()

        if 'hello' in txt:
            speak("Hello , How are you?")

        if 'you single' in txt:
            speak("Badey haraami ho betaa!")
