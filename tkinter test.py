from tkinter import *

root = Tk()

def MyClick():
    myLabel = Label(root, text = "Click Successful")
    myLabel.pack()

myButton = Button(root, text = "Click Me!", command = MyClick)
myButton.pack()


root.mainloop()