# # GUI = graphical user interface 
# # from tkinter import *

# # widgets = GUI elements: buttons, textboxes, labels, images 
# # window = serves as a container to hold or contain these widgets

# # window = Tk() #instantiate an instance of a window
# # window.geometry("420x420") #sets the width and height of the window
# # window.title("My first GUI program") #changing the title of window


# # PhotoImage is specifically designed for use with the Tkinter GUI library in Python. It's necessary because Tkinter itself doesn't have built-in support for displaying images directly from files. PhotoImage provides this functionality by allowing you to load images (in GIF and PGM/PPM formats) and then display them in Tkinter applications.
# # icon = PhotoImage(file="js.png")
# # window.iconphoto(True,icon) #changes the logo of window 

# # this config can be use for configuring many attributes of the window like border, width, height etc
# # window.config(background="#068c52")

# # window.mainloop() #place window on the computer screen, listen for events 

# # labels in python
# # from tkinter import *

# # # label = an area widget that holds text and/or an image within a window 

# # window = Tk()

# # photo = PhotoImage(file="js.png")

# # label = Label(window,text="Hello world",
# #               font=("Arial",40,"bold"),
# #               fg="green",
# #               bg="black",
# #               bd=10,
# #               relief=RAISED,
# #               padx=20,
# #               pady=20,
# #               image=photo,
# #               compound="bottom") #this instantiate the label

# # # this places the label at the top center
# # label.pack()
# # # if we want to customize the location of label then we can use this place method
# # # label.place(x=0,y=0)

# # window.mainloop()


# # buttons in python
# # from tkinter import *

# # count = 0

# # def click():
# #     global count
# #     count +=  1
# #     print(count)

# # window = Tk()

# # photo = PhotoImage(file="js.png")


# # button = Button(window,
# #                 text="click me!",
# #                 command=click,
# #                 font=("Comic Sans",30),
# #                 fg="blue",
# #                 bg="red",
# #                 activeforeground="blue",
# #                 activebackground="red",
# #                 state=ACTIVE,
# #                 image=photo,
# #                 compound="bottom")

# # button.pack()

# # window.mainloop()


# # entrybox
# # from tkinter import *

# # entry widget = textbox that accepts a single line of user input

# # def submit():
# #     username = entry.get()
# #     print("Hello "+username)
# #     entry.config(state=DISABLED)

# # def delete():
# #     entry.delete(0,END)

# # def backspace():
# #     entry.delete(len(entry.get()) -1,END)

# # window = Tk()

# # entry = Entry(window,
# #               font=("Arial",30),
# #               fg="yellow",
# #               bg="black",
# #               show="*")
# # entry.insert(0,"Spongebob")
# # entry.pack(side=LEFT)

# # submit_button = Button(window,
# #                 text="submit",
# #                 command=submit,
# #                 font=("Comic Sans",10),
# #                 fg="blue",
# #                 bg="red",
# #                 activeforeground="blue",
# #                 activebackground="red",)
# # submit_button.pack(side=RIGHT)

# # delete_button = Button(window,
# #                 text="delete",
# #                 command=delete,
# #                 font=("Comic Sans",10),
# #                 fg="blue",
# #                 bg="red",
# #                 activeforeground="blue",
# #                 activebackground="red",)
# # delete_button.pack(side=RIGHT)

# # backspace_button = Button(window,
# #                 text="backspace",
# #                 command=backspace,
# #                 font=("Comic Sans",10),
# #                 fg="blue",
# #                 bg="red",
# #                 activeforeground="blue",
# #                 activebackground="red",)
# # backspace_button.pack(side=RIGHT)


# # window.mainloop()


# # checkbox in python 
# # from tkinter import *

# # def display():
# #     if x.get() == 1:
# #         print("You agree")
# #     else:
# #         print("You don't agree")

# # window = Tk()

# # x = IntVar()

# # photo = PhotoImage(file="js.png")

# # check_button = Checkbutton(window,
# #                            text="I agree to something",
# #                            variable=x,
# #                            onvalue=1,
# #                            offvalue=0,
# #                            font=("Arial",20),
# #                            fg="yellow",
# #                            bg="red",
# #                            activeforeground="yellow",
# #                            activebackground="red",
# #                            command=display,
# #                            padx=25,
# #                            pady=10,
# #                            image=photo,
# #                            compound="left")
# # check_button.pack()

# # window.mainloop()


# # radio buttons
# # from tkinter import *

# # food = ["pizza","hamburger","hotdog"]

# # def order():
# #     if x.get() == 0 or x.get() == 1 or x.get() == 2:
# #         print("You have ordered "+food[x.get()])
# #     else:
# #         print("Huh!")

# # window = Tk()

# # x = IntVar()

# # for i in range(len(food)):
# #     radio_button = Radiobutton(window,
# #                                text=food[i],
# #                                variable=x, #group the radiobuttons together if they share the same variable
# #                                value=i, #assigns each radiobutton a different value
# #                                padx=25,
# #                                font=("Impact", 50),
# #                                indicatoron=0, #eliminate circle indicators 
# #                                width=10, #sets width of radio buttons
# #                                command=order)
# #     radio_button.pack(anchor=W)

# # window.mainloop()

# # scale in python
# # from tkinter import *

# # def submit():
# #     print("Today temprature is "+str(scale.get())+" degree celsius")

# # window = Tk()

# # scale = Scale(window,
# #               from_=100,
# #               to=0,
# #               length=600,
# #               orient=VERTICAL,
# #               font=("Consoles",20),
# #               tickinterval=10, #adds numeric indicators for value
# #               showvalue=1, #hide current value
# #               resolution=5, #increment of slider
# #               troughcolor="#69EAFF", #set the color of scale bar
# #               fg="#FF1C00",
# #               bg="#111111",
# #               activebackground="#111111"
# #               )

# # scale.set(((scale["from"]-scale["to"])/2)+scale["to"]) #set the scale default to middle value
# # scale.pack()

# # button = Button(window, text="Submit", command=submit)
# # button.pack()

# # window.mainloop()

# # listbox = A listing of selectable text items within it's own container
# # from tkinter import *

# # def submit():
# #     food = []
# #     print(listbox.curselection())
# #     for i in listbox.curselection():
# #         food.insert(i,listbox.get(i))
    
# #     print("You have ordered the following")
# #     for i in food:
# #         print(i)

# # def add():
# #     listbox.insert(listbox.size(),entry.get())
# #     listbox.config(height=listbox.size())
# #     entry.delete(0,END)

# # def delete():
# #     for i in reversed(listbox.curselection()):
# #         listbox.delete(i)    
# #     listbox.config(height=listbox.size())


# # window = Tk()

# # listbox = Listbox(window,
# #                   bg="#f7ffde",
# #                   font=("Constantia",20),
# #                   width=12,
# #                   selectmode=MULTIPLE)
# # listbox.pack()

# # listbox.insert(1,"pizza")
# # listbox.insert(2,"pasta")
# # listbox.insert(3,"garlic bread")
# # listbox.insert(4,"soup")
# # listbox.insert(5,"salad")

# # listbox.config(height=listbox.size()) #this dynamically sets the height of the listbox

# # entry = Entry(window)
# # entry.pack()

# # add_button = Button(window, text="add", command=add)
# # add_button.pack()

# # submit_button = Button(window, text="Submit", command=submit)
# # submit_button.pack()

# # delete_button = Button(window, text="delete", command=delete)
# # delete_button.pack()
# # window.mainloop()


# # messagebox in python
# # from tkinter import *
# # from tkinter import messagebox #import messagebox library

# # def click():
#     # messagebox.showinfo(title="An info message box",message="You are a person")
#     # messagebox.showwarning(title="Warning",message="You have a VIRUS!!!")
#     # messagebox.showerror(title="Error",message="Something went wrong")

#     # if messagebox.askokcancel(title="Ask Ok Cancel",message="Do you want to do the thing?"):
#     #     print("You did a thing")
#     # else:
#     #     print("You cancel a thing")
#     # if messagebox.askretrycancel(title="Ask Retry Cancel",message="Do you want to retry the thing?"):
#     #     print("You retry a thing")
#     # else:
#     #     print("You cancel a thing")
#     # if messagebox.askyesno(title="Ask Yes No",message="Do you like cake?"):
#     #     print("You like a cake")
#     # else:
#     #     print("You do not like a cake")
#     # if messagebox.askquestion(title="Ask Question",message="Do you like cake?") == "yes":
#     #     print("You like a cake")
#     # else:
#     #     print("You do not like a cake")
#     # answer =  messagebox.askyesnocancel(title="Ask Yes No Cancel",message="Do you like code?",icon="warning")
#     # if answer == True:
#     #     print("You like to code")
#     # elif answer == False:
#     #     print("You do not like to code")
#     # else:
#     #     print("You have dodged the question")

# # window = Tk()

# # button = Button(window,text='Click Me',command=click)
# # button.pack()
# # window.mainloop()


# # color chooser in python
# # from tkinter import *
# # from tkinter import colorchooser #submodule

# # def click():
# #     window.config(background= colorchooser.askcolor()[1])

# # window = Tk()
# # window.geometry("420x420")

# # button = Button(window,text='Click Me',command=click)
# # button.pack()

# # window.mainloop()

# # text Widget = functions like a text area. you can enter multiple lines of text
# # from tkinter import *

# # def submit():
# #     input = text.get("1.0",END)
# #     print(input)

# # window = Tk()

# # text = Text(window,
# #             bg="light yellow",
# #             font=("Ink Free",25),
# #             height=8,
# #             width=20,
# #             padx=20,
# #             pady=20,
# #             fg="purple")
# # text.pack()

# # button = Button(window,text="Submit",command=submit)
# # button.pack()
# # window.mainloop()

# # opening file from window
# # from tkinter import *
# # from tkinter import filedialog

# # def open_file():
# #     #askopenfilename returns the file path
# #     filepath = filedialog.askopenfilename(initialdir="C:\\Users\\pearl\\Documents", #this tells the python from which directory it should start looking for file
# #                                           title="Open The File Please",
# #                                           filetypes= (('text files','*.txt'),('all file','*.*'))) #this will create option to look only for text files and all files including
# #     file = open(filepath, "r")
# #     print(file.read())
# #     file.close()

# # window = Tk()

# # button = Button(window,text='Open',command=open_file)
# # button.pack()

# # window.mainloop()

# # saving a file
# # from tkinter import *
# # from tkinter import filedialog

# # def save_file():
# #     file = filedialog.asksaveasfile(initialdir="C:\\Users\\pearl\\Documents",
# #                                     defaultextension=".txt",
# #                                     filetypes=[
# #                                         ("Text file",".txt"),
# #                                         ("HTML file",".html"),
# #                                         ("All file",".*")
# #                                     ])
# #     # this getting text from Text Widget is not necessary we can also get text from user input thorugh terminal
# #     # textdata = input("How was your day? ")
# #     # this if statement is useful if we do not save any file and close the save dialog box 
# #     if file is None:
# #         return
# #     textdata = str(text.get(1.0,END))
# #     file.write(textdata)
# #     file.close()

# # window = Tk()

# # button = Button(window,text='Save',command=save_file)
# # button.pack()

# # text = Text(window)
# # text.pack()

# # window.mainloop()


# # menubar in python
# # from tkinter import *

# # def open_file():
# #     print("file has beeen opened")

# # def save_file():
# #     print("file has beeen saved")

# # def cut():
# #     print("You cut some text")

# # def copy():
# #     print("You copied some text")

# # def paste():
# #     print("You pasted some text")
    
# # window = Tk()

# # menubar = Menu(window)
# # window.config(menu=menubar)

# # file_menu = Menu(menubar, tearoff=0, font=("MV Boli",15))
# # menubar.add_cascade(label="file",menu=file_menu)
# # file_menu.add_command(label="Open", command=open_file)
# # file_menu.add_command(label="Save", command=save_file)
# # file_menu.add_separator()
# # file_menu.add_command(label="Exit", command=quit)

# # edit_menu = Menu(menubar, tearoff=0, font=("MV Boli",15))
# # menubar.add_cascade(label="edit",menu=edit_menu)
# # edit_menu.add_command(label="Cut", command=cut)
# # edit_menu.add_command(label="Copy", command=copy)
# # edit_menu.add_command(label="Paste", command=paste)

# # window.mainloop()


# # frame = a rectangular container to group and hold widgets
# # from tkinter import *

# # window = Tk()

# # frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# # frame.pack()

# # # if we don't want to name our buttons we can write like this
# # Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
# # Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
# # Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
# # Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

# # window.mainloop()

# #new wundow
# # from tkinter import *

# # def create_window():
# #     # new_window = Toplevel() #this create a window which is on top of first window, it is dependent on first window if we close the fist window it also closes.
# #     new_window = Tk() #this is independent window 
# #     window.destroy() #this closes our first window when we create new window
# # window = Tk()

# # Button(window,text="create new window",command=create_window).pack()

# # window.mainloop()


# # window tabs in python
# # from tkinter import *
# # from tkinter import ttk

# # window = Tk()

# # notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

# # tab1 = Frame(notebook) #new frame for tab1
# # tab2 = Frame(notebook) #new frame for tab2

# # notebook.add(tab1, text="Tab 1")
# # notebook.add(tab2, text="Tab 2")
# # notebook.pack(expand=True,fill="both") #expand = expand to fill any space not otherwise used, fill = fill space on x and y axis 

# # Label(tab1, text="Hello, this is tab1!!!", width=50, height=25).pack()
# # Label(tab2, text="Hello, this is tab2!!!", width=50, height=25).pack()

# # window.mainloop()


# # grid() = geometry manager that organizes widgets in a table-like structure in a parent widget
# # from tkinter import *

# # window = Tk()

# # Label(window, text="Enter Your Info", font=("Arial",25)).grid(row=0,column=0,columnspan=2)

# # Label(window, text="First Name: ", width=20).grid(row=1,column=0)
# # Entry(window).grid(row=1,column=1)

# # Label(window, text="Last Name: ").grid(row=2,column=0)
# # Entry(window).grid(row=2,column=1)

# # Label(window, text="Email: ").grid(row=3,column=0)
# # Entry(window).grid(row=3,column=1)

# # Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

# # window.mainloop()

# # progress bar 
# # from tkinter import *
# # from tkinter.ttk import *
# # import time

# # def start():
# #     GB = 100
# #     download = 0
# #     speed = 1
# #     while download < GB:
# #         time.sleep(0.05)
# #         bar["value"] += (speed/GB)*100
# #         download += speed
# #         percent.set(str(int((download/GB) * 100)) + "%")
# #         completed_GB.set(str(download)+'/'+str(GB)+" GB completed")
# #         window.update_idletasks()

# # window = Tk()

# # percent = StringVar()
# # completed_GB = StringVar()

# # bar = Progressbar(window,orient=HORIZONTAL,length=300)
# # bar.pack(pady=10)

# # percent_label = Label(window,textvariable=percent).pack()
# # GB_label = Label(window,textvariable=completed_GB).pack()

# # Button(window,text="download",command=start).pack()

# # window.mainloop()

# # canvas = widget that is used to draw graphs, plots, images in a window 
# # from tkinter import *

# # window = Tk()

# # canvas = Canvas(window,width=500,height=500)
# # # canvas.create_line(200,100,0,300,fill="red",width=5)
# # # points = [200,100,20,300]
# # # canvas.create_rectangle(points,fill="purple",outline="green",width=5)

# # # pogemon
# # points = [0,0,500,500]
# # canvas.create_arc(points,fill="red",extent=180,width=10)
# # canvas.create_arc(points,fill="white",extent=180,start=180,width=10)
# # canvas.create_oval(190,190,310,310,fill="white",width=10)
# # canvas.pack()

# # window.mainloop()


# # keyboard events 
# # from tkinter import *

# # def do_something(event):
# #     label.config(text= event.keysym)

# # window = Tk()

# # window.bind("<Key>",do_something)

# # label = Label(window,font= ("Helvetica",100))
# # label.pack()

# # window.mainloop()


# # mouse events 
# # from tkinter import *

# # def do_something(event):
# #     print("cordinates "+str(event.x)+","+str(event.y))

# # window = Tk()

# # # window.bind("<Button-1>",do_something)
# # # window.bind("<Button-3>",do_something)
# # # window.bind("<ButtonRelease>",do_something)
# # # window.bind("<Enter>",do_something)
# # # window.bind("<Leave>",do_something)
# # # window.bind("<Motion>",do_something)

# # window.mainloop()

# # drag & drop
# # from tkinter import *

# # def drag_start(event):
# #     widget = event.widget
# #     widget.startX = event.x 
# #     widget.startY = event.y

# # def drag_motion(event):
# #     widget = event.widget
# #     x = widget.winfo_x() - widget.startX + event.x
# #     y = widget.winfo_y() - widget.startY + event.y
# #     widget.place(x=x,y=y)

# # window = Tk()

# # label1 = Label(window,bg="red",width=10,height=5)
# # label1.place(x=0,y=0)

# # label1.bind("<Button-1>",drag_start)
# # label1.bind("<B1-Motion>",drag_motion)

# # label2 = Label(window,bg="blue",width=10,height=5)
# # label2.place(x=30,y=40)

# # label2.bind("<Button-1>",drag_start)
# # label2.bind("<B1-Motion>",drag_motion)

# # window.mainloop()


# # moving objects on window 
# # from tkinter import *

# # def move_up(event):
# #     label.place(x=label.winfo_x(),y=label.winfo_y() - 10)
    
# # def move_down(event):
# #     label.place(x=label.winfo_x(),y=label.winfo_y() + 10)
    
# # def move_left(event):
# #     label.place(x=label.winfo_x() - 10,y=label.winfo_y())
    
# # def move_right(event):
# #     label.place(x=label.winfo_x() + 10,y=label.winfo_y())
    

# # window = Tk()
# # window.geometry("500x500")

# # window.bind("<w>",move_up)
# # window.bind("<s>",move_down)
# # window.bind("<a>",move_left)
# # window.bind("<d>",move_right)
# # window.bind("<Up>",move_up)
# # window.bind("<Down>",move_down)
# # window.bind("<Left>",move_left)
# # window.bind("<Right>",move_right)

# # label = Label(window,bg="light green",width=5,height=3)
# # label.place(x=0,y=0)

# # window.mainloop()

# # moving objects on canvas
# # from tkinter import *
# # def move_up(event):
# #     canvas.move(my_image,0,-10)
    
# # def move_down(event):
# #     canvas.move(my_image,0,10)
    
# # def move_left(event):
# #     canvas.move(my_image,-10,0)
    
# # def move_right(event):
# #     canvas.move(my_image,10,0)

# # window = Tk()
# # window.bind("<w>",move_up)
# # window.bind("<s>",move_down)
# # window.bind("<a>",move_left)
# # window.bind("<d>",move_right)
# # window.bind("<Up>",move_up)
# # window.bind("<Down>",move_down)
# # window.bind("<Left>",move_left)
# # window.bind("<Right>",move_right)

# # canvas = Canvas(window,width=500,height=500)
# # canvas.pack()
 
# # photo = PhotoImage(file="js.png")
# # my_image = canvas.create_image(0,0,image=photo,anchor=NW)

# # window.mainloop()

# # animations in python
# # from tkinter import *
# # import time

# # # these are constants
# # WIDTH = 500
# # HEIGHT = 500
# # x_velocity = 3
# # y_velocity = 4

# # window = Tk()

# # canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# # canvas.pack()

# # oval = canvas.create_oval(3,3,120,120,fill="red",width=3)

# # while True:
# #     cordinates = canvas.coords(oval)
# #     oval_width = cordinates[2] - cordinates[0]
# #     oval_height = cordinates[3] - cordinates[1]
# #     print(cordinates)
# #     if(cordinates[0]>=(WIDTH-oval_width) or cordinates[0]<0):
# #         x_velocity = -x_velocity    
# #     if(cordinates[1]>=(HEIGHT-oval_height) or cordinates[1]<0):
# #         y_velocity = -y_velocity
# #     canvas.move(oval,x_velocity,y_velocity)
# #     window.update()
# #     time.sleep(0.01)

# # window.mainloop()

# # mutiple animation

# # from tkinter import *
# # from Ball import *
# # import time

# # WIDTH = 500
# # HEIGHT = 500

# # window = Tk()

# # canvas = Canvas(window,width=WIDTH,height=HEIGHT)
# # canvas.pack()

# # volleyball = Ball(canvas,0,0,100,1,1,"white")
# # tennisball = Ball(canvas,0,0,50,4,3,"green")

# # while True:
# #     volleyball.move()
# #     tennisball.move()
# #     window.update()
# #     time.sleep(0.01)

# # window.mainloop()


# # clock program of our own
# # from tkinter import *
# # import time

# # def string_represent(time,str):
# #     if len(str) == 1:
# #         time.config(text= "0"+str)
# #     else:
# #         time.config(text= str)

# # def update_sec():
# #     current_seconds = int(sec.cget("text"))
# #     time.sleep(1)
# #     current_seconds += 1
# #     sec_str = str(current_seconds)
# #     if sec_str == "60":
# #         string_represent(sec,"00")
# #         update_min()
# #     else:
# #         string_represent(sec,sec_str)

    
# # def update_min():
# #     current_min = int(min.cget("text"))
# #     current_min += 1
# #     min_str = str(current_min)
# #     if min_str == "60":
# #         string_represent(min,"00")
# #         update_hour()
# #     else:
# #         string_represent(min,min_str)

# # def update_hour():
# #     current_hour = int(hour.cget("text"))
# #     current_hour += 1
# #     hour_str = str(current_hour)
# #     if hour_str == "13":
# #         string_represent(hour,"01")
# #         update_zone()
# #     else:
# #         string_represent(hour,hour_str)

# # def update_zone():
# #     current_zone = desc.cget("text")
# #     if current_zone == "AM":
# #         desc.config(text = "PM")
# #     elif current_zone == "PM":
# #         desc.config(text = "AM")

# # window = Tk()

# # frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
# # frame.pack()

# # hour = Label(frame,text="12",font=("Consolas",25),width=3)
# # hour.pack(side=LEFT)
# # Label(frame,text=":",font=("Consolas",25),width=3).pack(side=LEFT)
# # min = Label(frame,text="59",font=("Consolas",25),width=3)
# # min.pack(side=LEFT)
# # Label(frame,text=":",font=("Consolas",25),width=3).pack(side=LEFT)
# # sec = Label(frame,text="45",font=("Consolas",25),width=3)
# # sec.pack(side=LEFT)
# # desc = Label(frame,text="PM",font=("Consolas",25),width=3)
# # desc.pack(side=LEFT)

# # while True:
# #     update_sec()
# #     window.update()

# # window.mainloop()


# # clock program using built-in functions
# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text = time_string)

#     time_label.after(1000,update)

# window = Tk()

# time_label = Label(window,font=("Arial",50),bg="pink",bd=5,relief=SUNKEN)
# time_label.pack()

# update()

# window.mainloop()