from tkinter import *
import random
import time

labels = list()
label_desc = None

winnging_list = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
]

def winning():
    for i in winnging_list:
        number = i[0]
        first_value = labels[number].cget("text")
        if first_value:
            filtered_list = list(filter(lambda x: labels[x].cget("text") == first_value,i))
            if len(filtered_list) == 3:
                label_desc.config(text= first_value+" Won")
                for k in i:
                    labels[k].config(bg="green")

def computer_choice():
    if len(label_desc.cget("text")) != 5:
        filteredlabels = list(filter(lambda x: not x.cget("text"),labels))
        num = random.randint(0,len(labels) - 1)
        label_comp = labels[num]
        if len(filteredlabels) != 0:
            if not label_comp.cget("text"):
                label_comp.config(text=computer_option) 
                time.sleep(0.5)
                winning()
            else:
                computer_choice()

def select(event):
    if len(label_desc.cget("text")) != 5:
        widget = event.widget
        if not widget.cget("text"):
            widget.config(text=player_option)
            time.sleep(0.5)
            winning()
            computer_choice()

def restart_game():
    for i in labels:
        i.config(text="")
        i.config(bg="whitesmoke")
        label_desc.config(text=f"Your choice is {player_option}")

def choose_option():
    global player_option , computer_option, window2, label_desc

    player_option = options[x.get()]
    for i in options:
        if i != options[x.get()]:
            computer_option = i
    window1.destroy()
    window2 = Tk()

    window2.geometry("600x500")
    window2.title("tic tac toe")

    label_desc = Label(window2,text=f"Your choice is {player_option}",pady=10,font=("Arial",30,"bold"))
    label_desc.pack()

    frame = Frame(window2,pady=20)
    frame.pack()
    
    list_label_num = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    for i in range(0,3):
        for j in range(0,3):
            globals()[f"label{list_label_num[i][j]}"] = Label(frame,text="",font=("Arial",60,"bold"),width=2,height=1,anchor="center",justify="center",bg="whitesmoke",bd=5,relief=GROOVE) 
            globals()[f"label{list_label_num[i][j]}"].grid(row=i,column=j)
            globals()[f"label{list_label_num[i][j]}"].bind("<Button-1>",select)
            labels.append(globals()[f"label{list_label_num[i][j]}"])
       
    button = Button(window2,text="Restart",font=("Arial",20,"bold"),bg="red",command=restart_game)
    button.pack()

    window2.mainloop()

options = ["X", "O"]

window1 = Tk()
window2 = None

player_option = None
computer_option = None
x = IntVar()

for i in range(len(options)):
    radio_button = Radiobutton(window1,
                               text=options[i],
                               variable=x,
                               value=i,
                               padx=25,
                               font=("Impact", 50),
                               indicatoron=0,  
                               width=10,
                               command=choose_option)
    radio_button.pack(side=LEFT)

window1.mainloop()