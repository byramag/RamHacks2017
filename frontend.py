from tkinter import *

def reward():
	print("Reward!")

def send():
	print("Sent message!")

def receive():
	print("Received message!")
	TK.after(5000, receive)

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

TK.after(5000, receive)
mainloop()