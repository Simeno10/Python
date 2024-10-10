from tkinter import *
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

image_width = photoImage.width()
image_height = photoImage.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity=-xVelocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()