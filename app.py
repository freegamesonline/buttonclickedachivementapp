from tkinter import *

root = Tk()

root.title("Button Clicked Achievement App")

root.wm_iconbitmap('icon1.ico')

def changeText():
    text.set("You clicked the button")

def resetText():
    text.set("You did not click the button")

text = StringVar()

label = Label(root, textvariable = text).pack()

text.set("You clicked the button")

clickButton = Button(root, text = "Click here to get an achievement", bd='5', command=changeText)
resetButton = Button(root, text = "Click here to lose your achievement", bd='5', command=resetText)

clickButton.pack(side='top')
resetButton.pack(side='top')

root.mainloop()
