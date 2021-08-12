from tkinter import *

win = Tk()

button1 = Button(win, text="Start", fg="blue",bg="yellow").pack(ipadx=12,ipady=10,padx="3cm",pady="10px")
button2 = Button(win, text="Start", fg="blue",bg="gray").pack(side="left")

win.mainloop()