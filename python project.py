from socket import timeout
from plyer import notification
import pyttsx3  
import datetime 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir ")   

    else:
        speak("Good Evening sir ")  

    speak("I am a system notifier i would help  you to remind your daily task and activities ")
wishMe() 
def notifyme(title ,message):
    notification.notify(
      title=title,
      message=message,
      app_icon= "C:\\Users\\Sagun\\OneDrive\\Desktop\\alexa\\icon.ico",
      timeout=10,
      
    ) 
    speak(title),
    speak(message),
hour = int(datetime.datetime.now().hour) 
now =datetime.datetime.now()
dt_string = now.strftime(" %m/%d/%Y %H:%M:%S")
	  
if hour>=11 and hour<12:
    notifyme("welcome sir","you are not studying")
    speak("the current date and time is .." )
    speak(dt_string)
if hour==8:
    notifyme("Welcome Sir !!","Please Take Your Breakfast ")
    speak("the current date and time is .." )
    speak(dt_string)
if hour==9:
    notifyme("Welcome sir !!","It's Time For Your English Learning ")
    speak("the current date and time is .." )
    speak(dt_string)  
if hour==10:
    notifyme("Welcome  Sir !!","Please Have A look at Your web devloppment course ")
    speak("the current date and time is .." )
    speak(dt_string)
if hour==12:
    notifyme("Welcome  Sir !!","Please Take Your Lunch and have a Rest ")
    speak("the current date and time is .." )
    speak(dt_string)
if hour==14:
    notifyme("Welcome Sir","Please Get Up and drink some water ")
    speak("the current date and time is .." )
    speak(dt_string)          
if hour==16:
    notifyme("Welcome  Sir !!","It's your playing time ")
    speak("the current date and time is .." )
    speak(dt_string)
if hour==20 :
    notifyme("Welcome  Sir !!","Please practice you DSA skills and solve problems ")
    speak("the current date and time is .." )
    speak(dt_string)
if hour<=24:
    notifyme("Good Night sir !!"," have a sweet sleep thank you ")
    speak("the current date and time is .." )
    speak(dt_string)
notifyme("sagunkumar","please drink a glass of  water")    
speak("thank you ...... have a nice day")


        
