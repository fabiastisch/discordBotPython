from tkinter import *

root = Tk()

# Create Stuff
myLabel = Label(root, text="Hello World")


def myClick():
    pass


myButton = Button(root, text="Click me", padx=50, pady=50, command=myClick)

# myLabel.pack()
# myLabel.grid(row=0,column= 0)


root.mainloop()
