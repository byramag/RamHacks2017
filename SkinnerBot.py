from tkinter import *
from socket import *

rewardCount = 0
inputStore = ""

def reward():
	rewardCount += 1

def send():
	inputStore = INPUTFIELD.get()

def process():	
	#process last output
	input = inputStore
	input = ""
	rewardTotal = rewardCount
	rewardCount = 0
	#associate reward with last output
	
	#process input
	
	
	#formulate output
	output = ""
	
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