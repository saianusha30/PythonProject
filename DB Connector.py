from tkinter import *


from PIL import ImageTk
window = Tk()
frame = Frame(window)
frame.place(x=700,y=100)
usernameLabel = Label(frame,text="username")
usernameLabel.grid(row=0,column=0)
usernameEntry = Entry(frame,width=30)
usernameEntry.grid(row=0,column=1)
passwordLabel = Label(frame,text="password")
passwordLabel.grid(row=1,column=0)
passwordEntry = Entry(frame,width=30)
passwordEntry.grid(row=1,column=1)
submitButton = Button(frame,text="submit")
submitButton.grid(row=1,column=2)
frame.pack()