#French Flash Card Program by Dalton Kinney 3/6/2022
#Gui interactable flash card program that will keep a list of vocab and definition to practice with
#Sort by category
from tkinter import *

#Create GUI
window = Tk()
#Create Menu Options
stBtn = Button(window, text="Start", fg='red')
stBtn.place(x=240, y=250)
exitBtn = Button(window, text="Exit", fg='red')
exitBtn.place(x=240, y=300)
#Create Label
title = Label(window, text="French Flash Card Program", fg='red', font=("Helvetica",25))
title.place(x=50, y= 200)
window.title("French Flash Card Program")
window.configure(width=500, height = 500)
window.configure(bg='red')
window.mainloop()
#Putting Window Center

#Actual Program stuff down here, activating buttons on screen