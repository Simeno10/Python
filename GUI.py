from tkinter import *


window = Tk()

window.geometry("420x420")
window.title("Yoooo first GUI")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#4275f5")

window.mainloop()