from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 200
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()
def dosth(event):
    #print("You pressed "+event.keysym)
    #label.config(text=event.keysym)
    print("You pressed " + str(event.x)+","+str(event.y))
def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,10)
def move_left(event):
    canvas.move(myimage,-10,0)
def move_right(event):
    canvas.move(myimage,10,0)


window = Tk()

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<s>", move_down)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Down>", move_down)

percent = StringVar()
text = StringVar()

window.bind("<Motion>", dosth)
window.bind("<Key>", dosth)
label = Label(window, font=("Helvetica", 100))
label.pack()

canvas = Canvas(window, height=500, width=500)
#blueLine = canvas.create_line(0,0,500,500, fill="blue", width=5)
#redLine = canvas.create_line(0,500,500,0, fill="red", width=5)
#canvas.create_rectangle(50,50,250,250)
points =[250,0,500,500,0,500]
#canvas.create_polygon(points,fill="green",outline="black", width=5)
#canvas.create_arc(0,0,500,500, style=PIESLICE, start=270, extent=180)
canvas.create_arc(0,0,500,500,fill="red", extent=180, width=10)
canvas.create_arc(0,0,500,500,fill="white", start=180, extent=180, width=10)
canvas.create_oval(190,190,310,310, fill="white", width=10)
canvas.pack()

icon2 = PhotoImage(file='icon2.png')
myimage = canvas.create_image(0,0,image=icon2, anchor=NW)

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="download", command=start).pack()

window.mainloop()
