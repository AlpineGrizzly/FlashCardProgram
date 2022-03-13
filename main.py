#French Flash Card Program by Dalton Kinney 3/6/2022
#Gui interactable flash card program that will keep a list of vocab and definition to practice with
#Sort by category
from tkinter import *

window = Tk()
window.resizable(0,0)
window.geometry("700x500")
window.configure(bg='grey')

#Destroy the window when quit is called
def quit():
    window.destroy()

#Creating Menu
title = Label(window, text="French Flash Card Program", fg='grey', font=("Times New Roman", 25))
title.pack_propagate(0)
title.pack(fill="both",expand=1)

stBtn = Button(window, text="Start", font=("Times New Roman", 15), fg='red')
stBtn.pack_propagate(0)
stBtn.pack(fill="both",expand=1)

exitBtn = Button(window, command = quit, text="Exit", font=("Times New Roman", 15), fg='red')
exitBtn.pack_propagate(0)
exitBtn.pack(fill="both",expand=1)
window.title("French Flash Card Program")
window.mainloop()


