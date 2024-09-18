from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser

count = 0
def click():
    global count
    count += 1
    print("You clicked button! ",count)
def submit():
    name = entry.get()
    print("Hello "+name)
    entry.config(state = DISABLED)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("You disagree")
def order():
    if (x.get() == 0):
        print("You ordered pizza!")
    elif (x.get() == 1):
        print("You ordered burger!")
    elif (x.get() == 2):
        print("You ordered sushi!")
    else:
        print("wtf man :{")
def submit2():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete2():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
def click2():
    #messagebox.showinfo(title='this is messagebox', message='You are a person')
    #messagebox.showwarning(title='WARNING', message='You have a virus!')
    #messagebox.showerror(title='ERROR', message='Something went wrong')
    #if messagebox.askokcancel(title='ask ok cancel', message='You want to do  it?'):
     #   print("yes, ok")
    #else:
     #   print("ok, cancel")
    #if messagebox.askretrycancel(title='ask ok cancel', message='You want to retry it?'):
     #   print("yes, ok, you retried")
    #else:
     #   print("ok, cancel")
    #if messagebox.askyesno(title="ask yes or no" ,message="Do you like cake?"):
     #   print("You like it")
    #else:
     #   print("You dont like it")
    #answer = messagebox.askquestion(title="Tell me", message="You like coding?")
    #print(answer)
    answer = messagebox.askyesnocancel(title="Tell me", message="You are fan of Star wars?", icon = 'warning')
    if (answer == True):
        print("Me too! :>")
    elif (answer == False):
        print("You motha! :<")
    else:
        print("You dodged! :/")
def click3():

    window.config(bg=colorchooser.askcolor()[1])
def submit3():
    input = text.get("1.0", END)
    print(input)

window = Tk()
icon = PhotoImage(file='icon.png')
icon2 = PhotoImage(file='icon2.png')

x=BooleanVar()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()

button = Button(window, command=submit3, text='click me')
button.pack()

listbox = Listbox(window,
                  bg="black",
                  fg="yellow",
                  font=("Constantia",20),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()
listbox.insert(1,"pizza")
listbox.insert(2,"hotdog")
listbox.insert(3,"salami")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit", command=submit2)
submitButton.pack()

addButton = Button(window,text="add", command=add)
addButton.pack()

deleteButton = Button(window,text="delete", command=delete2)
deleteButton.pack()

food = ["pizza", "burger", "sushi"]
foodImages = [PhotoImage(file='pizza.png'),PhotoImage(file='burger2.png'),PhotoImage(file='sushi.png')]
for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],
                              variable=x,
                              value=i,
                              padx=25,
                              font=("Impact", 50),
                              image=foodImages[i],
                              compound='left',
                              indicatoron=0,
                              width=375,
                              command=order)
    radiobutton.pack(anchor = W)

check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Arial",20),
                           fg="green",
                           bg="black",
                           activebackground="yellow",
                           activeforeground="red",
                           padx=25,
                           pady=10,
                           image=icon2,
                           compound='left'
                           )
check_button.pack()

entry = Entry(window,
              font=("Arial", 50),
              bg="green",
              fg="red",
              show="*")
entry.insert(0,"YOLO")
entry.pack(side=LEFT)
submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side = RIGHT)
delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side = RIGHT)
backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side = RIGHT)

button = Button(window,
                text="click me!",
                command=click,
                font=('Comic Sans',30),
                fg="black",
                bg="yellow",
                activeforeground="blue",
                activebackground="red",
                image=icon,
                compound='top')
button.pack()

#window.geometry("520x520")
window.title("Yoooo first GUI")


#label = Label(window,
#              text="Yoooo hello guys",
#              font=('Arial',40,'bold'),
#              fg='#eb4034',
#              bg='#2a8c41',
#              relief=SUNKEN,
#             bd=10,
#             padx=20,
#              pady=20,
#              image=icon,
#              compound='bottom')
#label.pack()
#label.place(x=210, y=210)


window.iconphoto(True,icon)
window.config(background="#4275f5")

window.mainloop()
