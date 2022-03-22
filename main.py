#French Flash Card Program by Dalton Kinney 3/6/2022
#Gui interactable flash card program that will keep a list of vocab and definition to practice with
#Sort by category
import tkinter
from tkinter import *
import time

window = Tk()
window.resizable(0,0)
window.geometry("700x500")
window.configure(bg='light blue')
window.title("FlashStudy Program")

def quit():
    window.destroy()

# Reads the cards into the program
def readCard():
    f = open('FrenchDeck.txt', 'r')
    f.close()

def closePopup(top):
    top.destroy()

def writeCard(frontText, backText):
    f = open('FrenchDeck.txt', 'a')
    f.write(frontText) #Get text from popup entry fields
    f.write(backText)
    f.close()

def addCard():
    top = Toplevel(window)
    top.geometry("200x150")
    labelf = Label(top, text="Enter the front card")
    labelf.pack()
    frontCard = Entry(top, width=50)
    frontCard.pack()
    labelb = Label(top, text="Enter the back card")
    labelb.pack()
    backCard = Entry(top, width=50)
    backCard.pack()
    submitBtn = Button(top, text="Add Card", command=writeCard(frontCard.get(), backCard.get()))
    submitBtn.pack()
    #exitBtn = Button(top, text="exit", command=closePopup(top))
    #exitBtn.pack()


def getFront():
    labelFront.configure(text="Bonjour, Dalton")

def getNext():
    labelFront.configure(text="Comment ca va?")

def checkAns():
    global entryAns
    string = entryAns.get()
    if(string == "Hello, Dalton"):
        labelFront.configure(text="Correct!")
        labelFront.after(3000, getNext)

    else:
        labelFront.configure(text="That was not correct, Try again!")
        labelFront.after(3000, getFront)

labelTitle = Label(window, height = 1,
                   width = 500,
                   text = "FlashStudy Program",
                   font = ("Arial", 15))
labelTitle.pack()

labelFront = Label(window,
                   height = 10, width=40,
                   text="Bonjour, Dalton",
                   font=("Arial", 15))
labelFront.place(relx=0.5,
                 rely=0.5,
                 anchor='center')

entryAns = Entry(window, width = 50)
entryAns.place(relx=0.5,
                rely=0.8,
                anchor='center')
entryAns.focus_set()

checkBtn = Button(window,
                  height = 1, width = 10,
                  text = "Check",
                  font = ("Arial", 10),
                  command = checkAns)
checkBtn.place(relx = 0.5,
               rely = 0.9,
               anchor = 'center')

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
                  font = ("Arial", 10),
                  command = addCard)
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



window.mainloop()




