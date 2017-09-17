from tkinter import *
import telnetlib

def reward():
	message = "1,"
	tn.write(bytearray(message, "ascii"))

def send():
	message = "0," + INPUTFIELD.get()
	tn.write(bytearray(message, "ascii"))

def receive():
	incoming = tn.read_very_lazy()
	if incoming != "b''":
		print(incoming)
	TK.after(5000, receive)

HOST = "127.0.0.1"
tn = telnetlib.Telnet(HOST) #can hang here
print("Connected successfully")

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