from tkinter import *
import time

y_value = 0
x_value = 0

def move():
  global y_value, x_value, direction
  label = Label(window, width=3, height=1, bg="green", relief=GROOVE)
  if direction == "down":
    y_value += 20
  elif direction == "up":
    y_value -= 20
  elif direction == "right":
    x_value += 20
  elif direction == "left":
    x_value -= 20
  value_y = y_value
  value_x = x_value
  label.place(x=value_x, y=value_y)
  labels.append(label)
  labels[0].destroy() 
  del labels[0] 
  window.after(50,move)      

def move_up(event):
  global direction

  if direction != "up":
    direction = "up"
    

def move_down(event):
  global direction

  if direction != "down":
    direction = "down"
    

def move_left(event):
  global direction

  if direction != "left":
    direction = "left"
  
def move_right(event):
  global direction

  if direction != "right":
    direction = "right"
  

window = Tk()
window.geometry("585x500")
window.resizable(False, False)

labels = list()

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


label = Label(window, width=3, height=1, bg="green", relief=GROOVE)
label.place(x=0, y=0)
labels.append(label)
label = Label(window, width=3, height=1, bg="green", relief=GROOVE)
label.place(x=0, y=0)
labels.append(label)
label = Label(window, width=3, height=1, bg="green", relief=GROOVE)
label.place(x=0, y=0)
labels.append(label)

direction = "down"

move()

window.mainloop()