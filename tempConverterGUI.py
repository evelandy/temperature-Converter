#!/usr/bin/env python3
"""evelandy/W.G.
Nov. 29 2018 8:42pm
temperature-converterGUI
Python36-32 
"""
from tkinter import *


def celsius():
    fahr = float(degree_entry.get())
    cfahr = (5 / 9) * (fahr - 32)
    cfahr = str(cfahr)
    label_c = Label(root, text="Fahrenheit converted to celsius is:\n {} "
                               "degrees celsius".format(cfahr), font=('bold', 18), fg='navy', bg='darkgray')
    label_c.place(x=40, y=200)


def fahrenheit():
    cel = int(degree_entry.get())
    fcel = str(round((9 / 5) * cel + 32, 2))
    label_f = Label(root, text="Celsius converted to fahrenheit is:\n {} "
                               "degrees fahrenheit".format(fcel), font=('bold', 18), fg='navy', bg='darkgray')
    label_f.place(x=50, y=200)


root = Tk()
root.iconbitmap(r'C:\Users\Prometheus\PycharmProjects\practice\py.ico')
root.geometry('500x500')

canvas = Canvas(root, bg='darkgrey')

instruct = "To convert a temperature simply type the\n temperature into the provided box,\n then click the " \
           "appropriate\n button to see your\n temperature converted.\nTo Quit press the Quit button"

label = Label(root, text='What is the temperature you would like to convert?', font=('bold', 16),
              fg='navy', bg='darkgrey')
instruct_label = Label(root, text=instruct, font=('Calibri', 12), fg='darkred', bg='darkgrey')

degree_entry = Entry(root, font=('Calibri', 21), width=7)

fahr_button = Button(root, text='Fahrenheit', font=('bold', 16), fg='mediumblue', command=fahrenheit)
cel_button = Button(root, text='Celsius', font=('bold', 16), fg='darkgreen', command=celsius)
quit_button = Button(root, text='QUIT', font=('bold', 16), fg='red', command=root.destroy)

canvas.pack(fill='both', expand=True)

label.place(x=10, y=10)
instruct_label.place(x=100, y=330)

degree_entry.place(x=190, y=50)

fahr_button.place(x=130, y=100)
cel_button.place(x=250, y=100)
quit_button.place(x=200, y=450)

root.mainloop()
