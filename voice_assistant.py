#Project:Voice Assistant
#Nmae:Ayusman Mishra
import pyttsx3
import datetime
import webbrowser
def main():
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',145)
    is_running=True
    print("Voice Assistant by Ayusman")
    engine.say("Hello User,I am your Assistant.")
    engine.runAndWait()
    while is_running:
       print("1. Get Time")
       print("2. Open Google")
       print("3. Exit")
       choice=input("Enter a command (1-3): ")
       if choice=="1":
           current_time=datetime.datetime.now().strftime("%I:%M %p")
           print(f"the time is:{current_time}")
           engine.say(f"The Time is {current_time}")
       elif choice=="2":
           print("Opening Google...")
           engine.say("Opening Google")
           engine.runAndWait()
           webbrowser.open("https://www.google.com")
       elif choice=="3":
           is_running=False 
       else:
           print("Invalid input,try again")
main()            