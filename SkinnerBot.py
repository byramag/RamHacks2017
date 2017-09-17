from tkinter import *
from socket import *

rewardCount = 0

def reward():
	rewardCount += 1

def send():
	print("hfwoueihg")

def process():
	
	
	
	print(output)
	TK.after(50, process)

TK = Tk()

TEXTS = Text(TK, width=50, height=5, state=DISABLED)
TEXTS.pack()

INPUTFIELD = Entry(TK, width=50)
INPUTFIELD.pack()
INPUTFIELD.focus_set()

MESSAGEBUTTON = Button(TK, text="Send", width=10, command=send)
MESSAGEBUTTON.pack()

REWARDBUTTON = Button(TK, text="Reward", width=10, command=reward)
REWARDBUTTON.pack()

TK.after(50, process)
mainloop()