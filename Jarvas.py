import pyttsx3
import datetime
import pyaudio
import webbrowser
import wikipedia
import os
import speech_recognition as sr
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
         speak("Good Afternoon!")
    else: 
        speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may i help u")

def takeCommand():
    #it takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"    
    return query
#sending Email        
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Enter the email_id from which u sending mail','password')
    server.sendmail('From which id u sending',to,content)
    server.close()
#writing content into file    
def writing(content):
    speak("At which file u want u write")
    text=takeCommand().lower()
    with open(f'{text}.txt',mode ='w') as file: 
                    file.write("Recognized text:") 
                    file.write("\n") 
                    file.write(content)
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.com") 
        #open photo    
        elif 'open photo' in query:
            photo_dir="C:\\Users\\Admin\\Pictures"
            pictures=os.listdir(photo_dir)
            speak("Which photo u want to open :")
            content=takeCommand()
            os.startfile(os.path.join(photo_dir,pictures[1]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")     
        elif 'exit' in query:
            break
        #open app which is install in your dekstop
        elif 'open visual studio code' in query:
            codePath="D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to "name of person" ' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="To whom u want to send"
                sendEmail(to,content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry can't send email")
        elif 'open notepad' in query:
            try:
                speak("What should i type?")
                content=takeCommand()
                writing(content)
            except Exception as e:
                speak("I am sorry!!")                       