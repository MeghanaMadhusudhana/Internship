import speech_recognition as aa
import pyttsx3

import datetime
import wikipedia
import pyjokes
import webbrowser
from tkinter import *
from pil import ImageTk,Image

import numpy
import cv2

listener=aa.Recognizer()

machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()
instruction='nill'

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech=listener.listen(origin)
            instruction=listener.recognize_google(speech)
            instruction=instruction.lower()
            if "boomer" in instruction:
                instruction=instruction.replace('boomer'," ")
                print(instruction)

    except:
        pass
    return instruction

class Widget:
    def __init__(self):
        root=Tk()
        root.title('boomer')
        root.geometry('520x320')
        img=cv2.imread("C:\\Users\\hp\\OneDrive\\Desktop\\boomer.jpg")





        img=ImageTk.PhotoImage(Image.open("C:\\Users\\hp\\OneDrive\\Desktop\\boomer.jpg"))
        panel=Label(root,image=img)
        panel.pack(side='right',fill='both',expand='no')
        userText=StringVar()
        userText.set('I am Boomer,How can i help you')
        userFrame=LabelFrame(root,text='boomer',font=('Railways',24,'bold'))
        userFrame.pack(fill='both',expand='yes')
        top=Message(userFrame,textvariable=userText,bg='black',fg='white')
        top.config(font=("Century Gothic",15,'bold'))
        top.pack(side='top',fill='both',expand='yes')
        btn=Button(root,text='run',font=('railways',10,'bold'),bg='blue',fg='white' ,command=self.clicked).pack(fill='x',expand='no')
        btn2=Button(root,text='Close',font=('railways',10,'bold'),bg='blue',fg='white',command=root.destroy).pack(fill='x',expand='no')
        root.mainloop()

    def clicked (self):
        print('working')

        def play_boomer():
            instruction=input_instruction()

            print(instruction)


            if 'time' in instruction:
                time=datetime.datetime.now().strftime('%I:%M%p')
                talk('Current time'+time)
            elif 'date' in instruction:
                date=datetime.datetime.now().strftime('%d /%m /%Y')
                talk("Today's date "+date)
            elif 'how are you' in instruction:
                talk('I am fine, how abot you')
            elif 'what is your name'in instruction:
                talk('I am boomer ,what can i do for you')
            elif  'who is' in instruction:
                human=instruction.replace('who is',"")
                info = wikipedia.summary(human,1)
                print(info)
                talk(info)
            elif "joke"in instruction:
                talk(pyjokes.get_joke())
            elif 'youtube' in instruction:
                talk('here you go')
                webbrowser.open('youtube.com')
            elif 'search' in instruction or 'play' in instruction:
                instruction=instruction.replace('search','')
                instruction=instruction.replace('play','')
                webbrowser.open(instruction)
            elif'weather' in instruction:
                instruction=instruction.replace('weather','')
                webbrowser.open(instruction)

            else:
                talk('please repeat')


        play_boomer()
if __name__=='__main__':
    widget=Widget()
