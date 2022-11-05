from tkinter import *

window = Tk()

canvas=Canvas(window,width=300,height=300)
canvas.pack()

img=PhotoImage(file='c:/temp/YJU_Logo.png')
canvas.create_image(150,150,image=img)

window.mainloop()

