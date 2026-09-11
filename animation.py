from tkinter import *
from ball import *
import time

WIDTH = 900
HEIGHT = 500
xVelocity = 1.5
yVelocity = 1

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bgImage = PhotoImage(file='space.png')
bg = canvas.create_image(0,0,image=bgImage, anchor=NW)

photoImage = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0,0,image=photoImage, anchor=NW)

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

image_width = photoImage.width()
image_height = photoImage.height()

while True:
    coordinates = canvas.coords(my_image)
    if (coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()
