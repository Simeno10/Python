from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
def move_up(event):
    label3.place(x=label3.winfo_x(), y=label3.winfo_y()-10)
def move_down(event):
    label3.place(x=label3.winfo_x(), y=label3.winfo_y()+10)
def move_left(event):
    label3.place(x=label3.winfo_x()-10, y=label3.winfo_y())
def move_right(event):
    label3.place(x=label3.winfo_x()+10, y=label3.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<s>", move_down)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
window.bind("<Down>", move_down)

icon = PhotoImage(file='icon.png')
label3 = Label(window, image=icon)
label3.place(x=0,y=0)

label = Label(window, bg="red", width=10, height=15)
label.place(x=0,y=0)

label2 = Label(window, bg="blue", width=10, height=15)
label2.place(x=100,y=100)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()

