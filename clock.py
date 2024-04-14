from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text = time_string)

    time_label.after(1000,update)

window = Tk()

time_label = Label(window,font=("Arial",50),bg="pink",bd=5,relief=SUNKEN)
time_label.pack()

update()

window.mainloop()

