#French Flash Card Program by Dalton Kinney 3/6/2022
#Gui interactable flash card program that will keep a list of vocab and definition to practice with
#Sort by category
import tkinter
from tkinter import *

window = Tk()
window.resizable(0,0)
window.geometry("700x500")
window.configure(bg='light blue')
window.title("FlashStudy Program")

def quit():
    window.destroy()
#@labelTitle: creates title for application
labelTitle = Label(window, height = 1,
                   width = 500,
                   text = "FlashStudy Program",
                   font = ("Arial", 15))
# @labelFront: will show the front of study cards
# @labelBack: will show the back of study cards
labelFront = Label(window,
                   height = 10, width=40,
                   text="Example front card here",
                   font=("Arial", 15))
labelFront.place(relx=0.5,
                 rely=0.3,
                 anchor='center')
labelBack = Label(window,
                  height = 10, width = 40,
                  text="Example back card here",
                  font=("Arial", 15))
labelBack.place(relx=0.5,
                rely=0.8,
                anchor='center')
# Buttons for application
# @startBtn: will shuffle through all cards that are in the deck
# @addcardBtn: will add a new card to the deck, prompting user to add front and back
# @editdeckBtn: allow the user to delete cards from deck
# @exitappBtn: exits out of application
startBtn = Button(window,
                  height = 2, width = 10,
                  text = "Start",
                  font = ("Arial", 10))
startBtn.place(relx = 0,
               rely = 0.3,
               anchor = 'w')
addcardBtn = Button(window,
                  height = 2, width = 10,
                  text = "Add Card",
                  font = ("Arial", 10))
addcardBtn.place(relx = 0.87,
                 rely = 0.3,
                 anchor = 'w')
editdeckBtn = Button(window,
                  height = 2, width = 10,
                  text = "Edit Deck",
                  font = ("Arial", 10))
editdeckBtn.place(relx = 0.87,
                  rely = 0.4,
                  anchor = 'w')
exitappBtn = Button(window,
                  height = 2, width = 10,
                  text = "Quit",
                  font = ("Arial", 10), command=quit)
exitappBtn.place(relx = 0,
                  rely = 0.4,
                  anchor = 'w')

labelTitle.pack()
#Application loop
window.mainloop()




