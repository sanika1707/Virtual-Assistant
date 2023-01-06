import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    elif hour>=16 and hour<19:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I'm Marauder, How may I help You?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}\n")
        
        except Exception as e:
            #print(e)
            print("Say that again please...")
            return "None"
        return query

if __name__ == "__main__":
    wishMe()
    
    x=1
    while x==1:    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
        
        elif "open hackerrank" in query:
            webbrowser.open("hackerrank.com")
        
        elif "play music" in query:
            music_dir = 'C:\\Users\\lenovo\\Desktop\\Omkar workspace\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  
       
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")
       
        elif "open code" in query:
            pathcode = "C:\\Users\\lenovo\\Appname\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(pathcode)
        elif 'quit' in query:
            x=5
