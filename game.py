## import libraries 
from random import randint
import pgzrun

WIDTH=500
HEIGHT=500
TITLE="Alien Game"
msg=""

## creating the sprites
alien=Actor("alien")

def draw():
    screen.clear()
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    screen.fill(color=(r,g,b))
    alien.draw()
    screen.draw.text(msg,center=(375,20),color="pink",fontsize=20)

def move_alien():
    alien.x=randint(30,WIDTH-30)
    alien.y=randint(30,HEIGHT-30)

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        msg="You got it"
        move_alien()
    else:
        msg="You missed it, try again"

move_alien()


pgzrun.go()