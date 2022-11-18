from tkinter import *
window = Tk()

photo = PhotoImage(file="C:/Users/USER/Desktop/dog.gif")
label1 = Label(window, image=photo)

label1.pack()

window.mainloop()
