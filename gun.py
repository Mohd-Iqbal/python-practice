from tkinter import *
import random

WIDTH = 800
HEIGHT = 600
GUN_WIDTH = 200
GUN_HEIGHT = 50
FIRE_WIDTH = 20
FIRE_HEIGHT = 30
FIRE_COLOR = "red"
GUN_COLOR = "green"
BACKGROUND_COLOR = "whitesmoke"
ENEMIES_COLOR = "purple"
fires = list()
enemies = list()


class Gun:

    def __init__(self):
        self.coordinates_vertical = list()
        self.coordinates_horizontal = list()
        self.bars = list()

        x1_vertical = (WIDTH/2) - (GUN_HEIGHT/2)
        y1_vertical = HEIGHT - GUN_WIDTH + 90
        x2_vertical = x1_vertical + GUN_HEIGHT
        y2_vertical = y1_vertical + GUN_WIDTH - 140
        self.coordinates_vertical.append([x1_vertical,x2_vertical, y1_vertical,y2_vertical])
        vertical = canvas.create_rectangle(x1_vertical,y1_vertical,x2_vertical,y2_vertical, fill=GUN_COLOR)
        self.bars.append(vertical)
           
        x1_horizontal = (WIDTH/2) - (GUN_WIDTH/2)
        y1_horizontal = HEIGHT - GUN_HEIGHT
        x2_horizontal = x1_horizontal + GUN_WIDTH
        y2_horizontal = y1_horizontal + GUN_HEIGHT
        self.coordinates_horizontal.append([x1_horizontal,x2_horizontal, y1_horizontal,y2_horizontal])
        horizontal = canvas.create_rectangle(x1_horizontal,y1_horizontal,x2_horizontal,y2_horizontal, fill=GUN_COLOR)
        self.bars.append(horizontal)


class Fire:

    def __init__(self):
        x1 = vertical_coords[0][0]
        x2 = vertical_coords[0][1]
        y1 = vertical_coords[0][2]
        x1_fire = x1 + ((x2 - x1) / 2) - (FIRE_WIDTH / 2) 
        y1_fire = y1 - 30
        x2_fire = x1_fire + FIRE_WIDTH
        y2_fire = y1_fire + FIRE_HEIGHT
        if len(fires) == 0:
            fire = canvas.create_rectangle(x1_fire,y1_fire,x2_fire,y2_fire, fill=FIRE_COLOR, tags="fire")
            canvas.tag_lower(fire)
            fire_data = [fire,x1_fire,x2_fire,y1_fire,y2_fire]
            fires.append(fire_data)            
        elif len(fires) != 0:
            if len(fires) == 1 and fires[0][4] < 455 or len(fires) > 1 and fires[-1][4] < 455:
                fire = canvas.create_rectangle(x1_fire,y1_fire,x2_fire,y2_fire, fill=FIRE_COLOR, tags="fire")
                canvas.tag_lower(fire)
                fire_data = [fire,x1_fire,x2_fire,y1_fire,y2_fire]
                fires.append(fire_data)            


class Enemies:

    def __init__(self):
        value_x = random.randint(0, int((WIDTH / FIRE_HEIGHT)) - 1) * FIRE_HEIGHT
        if value_x < 65:
            value_x = value_x + 75
        if value_x > 700:
            value_x = value_x - 90
        x1_enemy = value_x
        y1_enemy = 0
        x2_enemy = x1_enemy + FIRE_HEIGHT
        y2_enemy = y1_enemy + FIRE_WIDTH 
        enemy = canvas.create_rectangle(x1_enemy,y1_enemy,x2_enemy,y2_enemy, fill=ENEMIES_COLOR, tags="enemy")
        canvas.tag_lower(enemy)
        enemy_data = [enemy,x1_enemy,x2_enemy,y1_enemy,y2_enemy]
        enemies.append(enemy_data)

def fire():
    if len(fires) < 8:
        Fire()

def enemy():
    Enemies()
    window.after(1500,enemy)

def enemy_move():
    global vertical_coords,horizontal_coords

    #we can also create score label which will increase after hitting enemy and decrease after enemy pass the gun body 
    for enemy in enemies[:]:
        if not enemy[3] >= 700:
            canvas.move(enemy[0],0,10)
            enemy[3] += 10
            enemy[4] += 10
        else:
            canvas.delete(enemy[0])
            enemies.remove(enemy)

        check_borders() 

    for enemy in enemies:
        diff = enemy[2] - enemy[1]
        if int(enemy[4] - vertical_coords[0][3]) == 0 and int(vertical_coords[0][0])  <= enemy[1] <= int(vertical_coords[0][1]) - diff:
            canvas.delete(enemy[0])
            enemies.remove(enemy)
        elif int(enemy[4] - horizontal_coords[0][3]) == 0 and int(horizontal_coords[0][0])  <= enemy[1] <= int(horizontal_coords[0][1]) - diff:
            canvas.delete(enemy[0])
            enemies.remove(enemy)


    window.after(50,enemy_move)
    

def fire_move():

    if len(fires) > 0:
        for fire in fires[:]:
            if not fire[4] < -100:
                canvas.move(fire[0],0,-10)
                fire[3] -= 10 
                fire[4] -= 10 
            else:
                canvas.delete(fire[0])
                fires.remove(fire)

    window.after(50,fire_move)

def check_borders():
    enemies_to_remove = []
    fires_to_remove = []
    

    for fire in fires[:]:
        fire_bbox = canvas.bbox(fire[0]) 
        for enemy in enemies[:]:
            enemy_bbox = canvas.bbox(enemy[0])
            if fire_bbox and enemy_bbox:
                overlapping_items = canvas.find_overlapping(*fire_bbox)
                if enemy[0] in overlapping_items:
                    enemies_to_remove.append(enemy)
                    fires_to_remove.append(fire)


    for enemy in enemies_to_remove:
        canvas.delete(enemy[0])
        enemies.remove(enemy)

    for fire in fires_to_remove:
        canvas.delete(fire[0])
        fires.remove(fire)


def move_left(gun):

    bars = gun.bars
    coordinates_hori = gun.coordinates_horizontal
    coordinates_ver = gun.coordinates_vertical

    if not coordinates_hori[0][0] <= 0:
       canvas.move(bars[0],-20,0)
       canvas.move(bars[1],-20,0)
       coordinates_hori[0][0] -= 20
       coordinates_hori[0][1] -= 20
       coordinates_ver[0][0] -= 20
       coordinates_ver[0][1] -= 20

def move_right(gun):
    
    bars = gun.bars
    coordinates_hori = gun.coordinates_horizontal
    coordinates_ver = gun.coordinates_vertical

    if not coordinates_hori[0][1] >= WIDTH:
       canvas.move(bars[0],20,0)
       canvas.move(bars[1],20,0)
       coordinates_hori[0][1] += 20
       coordinates_hori[0][0] += 20
       coordinates_ver[0][1] += 20
       coordinates_ver[0][0] += 20



window = Tk()
window.title("GUN GAME")
window.resizable(FALSE,FALSE)

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg=BACKGROUND_COLOR)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

gun = Gun()
vertical_coords = gun.coordinates_vertical
horizontal_coords = gun.coordinates_horizontal

window.bind("<Left>", lambda event: move_left(gun))
window.bind("<Right>", lambda event: move_right(gun))
window.bind("<KeyRelease-Up>", lambda event: fire())

enemy()
enemy_move()
fire_move()

window.mainloop()