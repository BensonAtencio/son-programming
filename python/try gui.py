from tkinter import *

Bgui = Tk()
Bgui.geometry("500x500")
Bgui.title("Student Management System")

x1 = Entry(Bgui)
x1.grid(row=1, column=1)
x2 = Entry(Bgui)
x2.grid(row=2, column=1)
x1.get()
x2.get()

label = Label(Bgui, text="                  ")
label1 = Label(Bgui, text="Student Number: ")
label2 = Label(Bgui, text="Student Name: ")

label.grid(row=0, column=0)
label1.grid(row=1, column=0)
label2.grid(row=2, column=0)

def hello():
    label = Label(Bgui, text="Student Number: "+ x1.get())
    label1 = Label(Bgui, text="Student Name: "+ x2.get())
    label.grid(row=4, column=0)
    label1.grid(row=5,column=0)

button = Button(Bgui, text="Show", command=hello, fg="blue")
button.grid(row=6, column=0)

Bgui.mainloop()