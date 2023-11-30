import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
#function of speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function to wish 
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>= 4 and hour<=12):
        speak("good moring sir ")
    elif(hour>12 and hour<16):
        speak("good afternoon sir")
    elif(hour>=16 and hour<20):
        speak("good evening sir")
    else:
        speak("good night sir")  
    speak("chirayu boss  here i am  at your service  ")

def takecommand():
    '''it takes microphone input from 
    the user to return suitable output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:  
        print('LISTENING.......')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f'user said:{query}\n')

    except Exception as e:
       # print(e)
        speak("say that again sir ")
        return "none"
    return query
#main function 
if __name__=="__main__":
    wishme()
    #logic for tasks
    while True:
            query=takecommand().lower()


            if wikipedia in query:
                speak("searching wikipedia")
                query =query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak ("according to wikipedia")
                speak(results)
                print(results)

            elif "open youtube" in query: 
                webbrowser.open("youtube.com")   

            elif "open google" in query: 
                webbrowser.open("google.com") 

            elif 'play music' in query:
                music_dir='your music file location in future'  
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif "the time " in query:
                strTime=datetime.datetime.now().strftime("%H%M%S") 
                speak(f"sir the time is {strTime}")   

            elif "open code " in query:
                codePath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
