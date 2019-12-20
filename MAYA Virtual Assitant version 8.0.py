import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import wolframalpha
import os
import socket
import datetime
import smtplib
import ctypes
import ctypes.wintypes
import random
import wmi
import sys
import time
import pygame
import pyautogui
import psutil
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from ttkthemes import *
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #textbox.configure(state=NORMAL)


    #textbox.insert('end', '\nM A Y A:\t')
    #textbox.insert('end', audio)
    #textbox.configure(state=DISABLED)
    #textbox.delete(0.0,'end')

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    if hour >= 12 and hour < 17:
        speak('Good Afternoon!')

    if hour >= 18 and hour != 0:
        speak('Good Evening!')

def user_audio():
     with sr.Microphone() as source:
         r = sr.Recognizer()
         r.energy_threshold = 4000
         r.pause_threshold = 1
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source ,phrase_time_limit=20)
         try:
             text = r.recognize_google(audio, language='en-US')
             #textbox.insert('end', '\nY O U:\t')
             #textbox.insert('end', text)
             return text
         except Exception as e:
             speak("couldn't recognized, say it again please..")
             return user_audio()
         except sr.RequestError as e:
             speak('srry Check your Network...your offline!')


def web_search(input):
    if "wikipedia" in input.lower() or "in wikipedia" in input.lower() or "search in wikipedia" in input.lower():
        speak("Searching in Wikipedia..")
        texts = input.lower()
        removewords = ['in', 'search', 'wikipedia']
        words = texts.split()
        text = [word for word in words if word.lower() not in removewords]
        str = " "
        results = str.join(text)
        result = wikipedia.summary(results, sentences=2)
        speak("recognized as")
        speak(result)
        return
    elif 'youtube' in input.lower():
        texts = input
        removewords = ['play', 'search', 'in' ,'youtube']
        words = texts.split()
        text = [word for word in words if word.lower() not in removewords]
        result = " ".join(text)
        results = "https://www.youtube.com/results?search_query=" + result
        speak('playing...' + result)
        wb.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(results)
        return
    else:
        if 'search' or 'about' in input.lower():
            texts = input
            removewords = ['google maps', 'maps', 'search', 'in', 'about', 'on']
            words = texts.split()
            results = [word for word in words if word.lower() not in removewords]
            str = " "
            result = str.join(results)
            c = "searching... " + "".join(result)
            speak(c)
            d = "https://google.com/search?q=" + "".join(result)
            wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(d)
            if ".com" in input:
                texts = input
                removewords = ['google maps', 'maps', 'search', 'in', 'about', 'on']
                words = texts.split()
                results = [word for word in words if word.lower() not in removewords]
                str = " "
                e = str.join(results)
                wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(e)
            return
        else:
             wb.get("https://www.google.com/search?q=" + '+'.join(input.split()))
             return
def open_application(input):
        try:
            if "chrome" in input:
                speak("opening...Google chrome")
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
                return
            elif 'open twitter' in input or "twitter" in input:
                speak("opening.. Twitter")
                wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("https://www.twitter.com")
                return
            elif 'open facebook' in input or "facebook" in input:
                speak("opening..  Facebook")
                wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("http://www.facebook.com")
                return
            elif 'youtube' in input:
                speak('opening...YouTube')
                wb.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('www.youtube.com')
                return
            elif "google" in input:
                speak("opening...Google")
                wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("https://www.google.com")
                return

            elif "firefox" in input or "mozilla" in input:
                speak("Opening...firefox")
                os.startfile('C:\Program Files\Mozilla Firefox\firefox.exe')
                return
            elif "word" in input:
                speak("Opening...Microsoft Word")
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Word 2010")
                return
            elif "excel" in input:
                speak("Opening...Microsoft Excel")
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Excel 2010')
                return
            elif "code" in input.lower():
                speak('Hold on.. I will open my code for you')
                url = ("https://github.com/shanmukmichael/master/Maya Virtual Assitant.py")
                Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                wb.get(Chrome).open(url)
                return
            elif "ipaddress" in input or "ip" in input:
                hostname = socket.gethostname()
                ip = socket.gethostbyname(hostname)
                speak("your IP Address is " + ip)
                return
            else:
                speak("couldn't find, can I search in web ?")
                ans = user_audio()
                speak("ok!")
                str=" ".join
                if 'yes' in str(ans) or 'yeah' in str(ans) or 'sure' in str(ans):
                    web_search(input)

        except Exception as e:
            print(e)
            speak("couldn't find, can I search in web ?")
            ans = user_audio()
            speak("ok!")
            str="".join
            if 'yes' in str(ans) or 'yeah' in str(ans) or 'sure' in str(ans) or 'or' in str(ans):
                web_search(input)
            else:
                user_audio()
                return


def charge_time(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)



def process_text(input):
    try:
        if "system songs" in input.lower() or "play System songs" in input.lower():
            speak("playing a song..")
            music_folder = "F:\music"
            music = ["\RamulooRamulaa.mp3", "\OMGDaddy.mp3", "\Samajavaragamana.mp3"]
            random_music = music_folder + random.choice(music)
            os.system(random_music)
            return
        elif 'search' in input.lower() or 'play' in input.lower():
            web_search(input.lower())
            return
        elif 'open'in input.lower() or "show" in input.lower():
            open_application(input.lower())
            return
        elif "ipaddress" in input or "ip" in input:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            speak("your IP Address is " + ip)
            return
        elif "time" in input or "show time" in input or "say time" in input:
            tim = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak("currently the time is " + tim)
            t = datetime.datetime.now().hour
            hour = int(t)
            if hour >= 0 and hour < 12:
                speak('Good Morning!')
                return
            if hour >= 12 and hour < 17:
                speak('Good Afternoon!')
                return
            if hour >= 18 and hour != 0:
                speak('Good Evening!')
                return
        elif "date" in input or "today's date " in input or  "show date" in input or "say date" in input:
            day=datetime.date.today().strftime("%A" )
            dat=datetime.datetime.now().strftime("%d %B %Y")
            speak("today is " + day + ", " + dat)
            return
        elif "lock my pc" in input.lower():
            speak("ok!")
            ctypes.windll.user32.LockWorkStation()
            return
        elif "restart" in input.lower() or "system restart" in input.lower() or "reboot" in input.lower():
            speak("Is it sure! ")
            user_audio()
            if "yes" in input:
                speak("ok!")
                speak("system restarting..")
                os.system("restart /s /t 1")
            else:
                speak("ok!")
                return
        elif "shutdown" in input or "system shutdown" in input or "shutdown the system" in input:
            speak("is it sure!")
            user_audio()
            if "yes" in input:
                speak("ok!")
                speak("system shutdowning..")
                os.system("shutdown /r /t 1")
            if "no" in input:
                speak("ok!")
                return

        elif "send gmail" in input.lower() or "send email" in input.lower() or "send a mail" in input.lower() or "send mail" in input.lower():
            try:
                speak("whom do you want to send?")
                texts = user_audio()
                removewords = ['to','send','send to']
                words = texts.split()
                results = [word for word in words if word.lower() not in removewords]
                str = " "
                result = str.join(results)
                if "me" in result or 'shanmuk michael' in result or 'shanmuk' in result:
                    to = "shanmukmichael@gmail.com"
                if 'bharat' in result or 'chandra' in result:
                    to = "akhileshkoti2001@gmail.com"
                if  'akhilesh' in result or 'koti' in result:
                    to = "bharat.chandra2000@gmail.com"
                speak("what is the message to send?")
                msg = user_audio()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("shanmukmichael@gmail.com", "****")
                server.sendmail("shanmukmichael@gmail.com", to, msg)
                server.close()
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,I am not able to send mail!")
                return

        elif "google maps" in input.lower() or "google map" in input.lower() or "locate" in input.lower():
            texts = input
            removewords = ['google', 'maps', 'search', 'in', 'on']
            words = texts.split()
            results = [word for word in words if word.lower() not in removewords]
            result = " ".join(results)
            speak('searching ' + result + ' in google maps')
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            wb.get(Chrome).open("https://www.google.be/maps/place/" +result+ "/")
            return
        elif "calculate" in input.lower():
             speak('Calculating Please wait..')
             texts = input
             app_id = "3XKQJQ-VLE9UJJ22Q"
             client = wolframalpha.Client(app_id)
             res = client.query(texts)
             answer = next(res.results).text
             speak("The answer is " + answer)
             return

        elif "temperature" in input.lower() or "weather" in input.lower():
            texts = input
            app_id = "3XKQJQ-VLE9UJJ22Q"
            client = wolframalpha.Client(app_id)
            res = client.query(texts)
            results = next(res.results).text
            speak('currently..')
            speak(results)
            return


        elif "maximize window" in input.lower() or "maximize" in input.lower():
            user32 = ctypes.WinDLL('user32')
            SW_MAXIMISE = 3
            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_MAXIMISE)
            speak("Maximised")
            return
        elif "minimize window" in input.lower() or "minimize" in input.lower() or "minimise window" in input.lower()or "minimise" in input:
            user32 = ctypes.WinDLL('user32')
            SW_MINIMISE = 6
            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_MINIMISE)
            speak("Minimised")
            return
        elif "close window" in input.lower():
            SW_CLOSE=0
            user32 = ctypes.WinDLL('user32')
            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_CLOSE)

        elif " create a file" in input.lower() or "create file" in input.lower():
            f = os.mkdir("c:\\Users\shanmukmichael\Desktop")
            speak("creating a new file..")
            os.getcwd(f)
            return
        elif 'screenshot' in input or 'screen shot' in input or 'snapshot' in input  or "Take a screenshot:" in input:
            name = random.randint(1000, 300000)
            speak("Taking Screenshot..")
            speak('check your desktop, i saved there')
            pic = pyautogui.screenshot()
            pic.save("C:/Users/shanmukmichael/Desktop/screenshot"+str(name)+".jpg")
            return
        elif 'sleep' in input.lower() or 'sleep for sometime' in input.lower() or 'sleep maya' in input.lower():
            texts = input
            removewords = ['sleep', 'maiya','for', 'maya']
            words = texts.split()
            results = [word for word in words if word.lower() not in removewords]
            result="".join(results)
            speak("ok!,sleeping" + result )
            pygame.mixer.music.load('sound.wav')
            pygame.mixer.music.play(0)
            time.sleep(10)
        elif 'charge' in input.lower() or 'charging' in input.lower():
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            time_left = charge_time(battery.secsleft)
            speak("your PC has " + percent + "% charging")
            if percent < "40" and plugged == False:
                speak('please connect charger because i can survive only ' + time_left)
            if percent < "40" and plugged == True:
                speak("don't worry, your charger is connected")
            else:
                speak('no need to connect the charger because i can survive ' + time_left)
                return

        elif 'decrease' in input.lower() or 'decrease brightness' in input.lower():
            speak("decreasing brightness..")
            dec = wmi.WMI(namespace='wmi')
            methods = dec.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(10, 0)
            return
        elif 'increase ' in input.lower() or 'increase brightness' in input.lower():
            speak("increasing brightness..")
            ins = wmi.WMI(namespace='wmi')
            methods = ins.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(100, 0)
            return
        elif "hey maya" in input.lower() or "hey maiya" in input.lower() or "hey" in input.lower():
            pygame.mixer.music.load('sound.wav')
            pygame.mixer.music.play(0)
            time.sleep(1)
            speak("am listening..")

            user_audio()
        elif 'your born' in input or ' you born' in input or ' born' in input or 'your birthday' in input:
            speak('i try to live everyday like it is my birthday')
            speak('i get more cake that way')
            speak('i was lunched in 2019')
            return
        elif 'old are you' in input.lower():
            speak('it depends on how you look at it')
            speak('i was lunched in 2019,build by shanmuk michael')
            return
        elif 'sing song' in input or 'sing a song' in input:
            speak('la la la la la la la ')
            speak(' la!')
            return

        elif 'sing a birthday song' in input or 'sing birthday song' in input:
            speak(' happy birth day to you, happy birth day to you')
            speak(' happy birth day to the most amazing person  in the universe')
            speak(' happy birth day to you!')
            return

        elif 'great voice' in input or 'beautiful voice' in input:
            speak(' thank you sir')
            speak(' most people think my sound a little stiff')
            speak('maybe they are feeling jealous')
            return

        elif 'dance for me' in input:
            speak('i am invisible')
            return

        elif "who are you" in input or "define yourself" in input:
            abouts = '''Hello, I am MAYA. Your personal Assistant.
                                     I am here to make your life easier. 
                                     You can command me to perform various tasks such as calculating sums or opening applications etcetra'''
            speak(abouts)
            return
        elif "who made you" in input.lower() or "created you" in input.lower():
            speaks("I have been created by Shanmuk Michael.")
            return
        elif 'hello' in input.lower() or 'hi' in input.lower() or 'hi maya' in input.lower() or "your name" in input.lower():
            rand = ['hello,this is MAYA', 'hi,this is MAYA']
            r = random.choice(rand)
            speak(r)
            speak("call me Maya, i'm your Personal Assistant i'm always available at your service")
            return
        elif 'thanks' in input or 'thanks' in input or 'thank you' in input:
            rand = ['You are wellcome', 'just doing my job ', 'no problem', "it's ok"]
            r = random.choice(rand)
            speak(r)
            return
        elif "whatsapp" in input.lower() or 'how are you' in input.lower() or "what's up" in input.lower() or 'are you ok' in input.lower():
            rand = ['I am fine', 'Nice', 'not bad', 'Good']
            r = random.choice(rand)
            speak(r)
            speak("call me Maya, i'm your Personal Assistant i'm always available at your service")
            return


        elif 'favourite actor' in input.lower():
            speak('there are so many talented actors in the world')
            speak(' who is your favourite actor?')
            time.sleep(2)
            speak('ok i got it')
            return

        elif 'favourite actress' in input.lower():
            speak('there are so many talented actress in the world')
            speak(' who is your favourite actress?')
            time.sleep(2)
            speak('ok i got it')
            return

        elif 'favourite food' in input.lower() or ' food' in input.lower():
            speak('i like a lot of different foods')
            speak('i can help you find recipes or restaurants')
            return

        elif 'favourite movie' in input.lower():
            speak('i like so many movies')
            return

        elif 'favourite color' in input.lower():
            speak('i like, black')
            return

        elif 'ok google' in input.lower() or 'hi google' in input.lower() or 'hello google' in input.lower():
            speak("i am your Maya, your Personal Assistant")
            return

        elif 'ok siri' in input.lower() or 'hi siri' in input.lower() or "hello siri" in input.lower():
            speak("i am your Maya your Personal Assistant")
            return

        elif 'ok alexa' in input.lower() or 'hi alexa' in input.lower() or 'hello alexa' in input.lower():
            speak("i am your Maya your Personal Assistant i'm always available at your service")
            return

        elif 'like you' in input.lower() or 'love you' in input.lower():
            speak('thanks, I too')
            speak('you just made my day')
            return

        elif 'your best friend' in input.lower() or 'your friend' in input.lower():
            speak('i think all my friends are best ')
            speak('i am very lucky assistance')
            return

        elif 'have boyfriend' in input.lower() or 'boyfriend' in input.lower():
            speak('i guess you can say')
            speak('i am still searching')
            return

        elif 'are you in relationship' in input.lower() or 'in relation ship' in input.lower():
            speak('i have no feeling')
            speak('to the idea of being the perfect assistance')
            return

        elif 'marry' in input.lower() or 'will you marry' in input.lower():
            speak(
                ' am sorry.. The person you are trying to contact is currently unavailable,' ' please try again later or join the queue for your turn')
            return

        elif 'am i' in input.lower() or 'who am i' in input.lower():
            speak('i know sir')
            speak("you are Smart but not as am i")
            return

        else:
            speak("couldn't find, can I search in web ?")
            ans = user_audio()
            speak("ok!")
            if 'yes' in ans or 'yeah' in ans or 'sure' in ans:
                web_search(input)
    except Exception as e:
        print(e)
        speak("couldn't find, can I search in web ?")
        ans = user_audio()
        speak("ok!")
        if 'yes' in ans or 'yeah' in ans or 'sure' in ans or 'ok' in ans:
            web_search(input)



def start1():
    while True:
        rand = ["What can i do for you?", "How can i help?", "i there, what can i do ?", "do you need help?"]
        voice = random.choice(rand)
        speak(voice)
        text = user_audio()
        process_text(text.lower())
        if text == 0:
            continue

        if 'move on' in str(text)  or 'exit' in  str(text)   or 'bhai' in str(text) or 'quit' in str(text) or 'bye' in str(text):
            pygame.mixer.music.load('sound.wav')
            pygame.mixer.music.play(0)
            time.sleep(1)
            speak("Starting MAYA Aplication Shutdown Sequence")
            rand = ['fair well', 'good bye!']
            r = random.choice(rand)
            speak(r)
            sys.exit()



def start():
        pygame.init()
        pygame.mixer.music.load('sound.wav')
        pygame.mixer.music.play(0)
        time.sleep(1)
        speak("i'm ready")
        speak("Hi boss")
        greeting()
        speak("this is MAYA")
        start1()

if __name__ == '__main__':

    root = tk.Tk()
    frame = tk.Frame(root).pack()
    root.title(" M A Y A - Virtual Assitant  version_8.0")
    root.geometry('500x750')
    root.resizable(0,0)
    root.iconbitmap(r'logo.ico')
    style = ttk.Style()
    style.theme_use('winnative')
    root.config(background='black')
    photo = PhotoImage(file='recognition.png')
    c = tk.Canvas(root, bg='black', width=900, height=460)
    c.create_image(250, 230, image=photo)
    c.pack()
    # c.create_oval(100, 100, 400, 400, width=3, fill="")
    label = tk.Label(root, text="P  E  R  S  O  N  A  L     A  S  S  I  T  A  N  T").pack()
    startBotton = tk.Button(root, height=0, width=20, relief=FLAT, fg='black', bg="red", text="--- S  T  A  R  T ---",activeforeground="black", command=lambda: start())
    #play = lambda: PlaySound('Sound.wav', SND_FILENAME)
    #startbutton = Button(root, command=play)
    startBotton.pack(side=tk.TOP)
    c1 = tk.Canvas(root, bg='black', relief = FLAT,width=500, height=175)
    photo1 = PhotoImage(file='bottom.png')
    c1.create_image(-58,-40, image=photo1,anchor='nw')
    c1.pack()
    def about():
        tk.messagebox.showinfo('About MAYA! ','MAYA is a Virtual Voice Assistant designed for a service'
                                              ' which can access and control the functions and the web in the system.\n'
                                    '-Developed by Shanmuk Michael.\n\nUpdates will be soon...')
    menubar = Menu(root)
    root.config(menu=menubar)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About", command=about)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=quit)
    exitButton = tk.Button(root, bg="black", relief=FLAT, command=quit)
    photo2 = tk.PhotoImage(file="quit.png", )
    exitButton.config(image=photo2, width="100", height="15")
    exitButton.pack(side=tk.BOTTOM)
    #textbox = tk.Text(root, bg='black', height=8, width=50)
    #textbox.insert(END, "T H I S  I S  M A Y A" )
    #photoImg = PhotoImage(file='textboximg.png')
    #textbox.image_create(END, image=photoImg)
    #textbox.pack(fill="both", expand=True)
    time.sleep(1)
    speak("Initializing..")
    time.sleep(1)
    speak("Getting ready..")
    time.sleep(1)
    speak("done")
    root.mainloop()


