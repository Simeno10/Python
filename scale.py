from tkinter import *

def submit():
    print("The temperature is "+ str(scale.get())+" degrees C")

window = Tk()
hotImage = PhotoImage(file="fire2.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=200,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
              resolution=5,
              troughcolor="blue",
              fg="red",
              bg="black")

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

coldImage = PhotoImage(file="ice2.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text='submit', command=submit, )
button.pack()


window.mainloop()