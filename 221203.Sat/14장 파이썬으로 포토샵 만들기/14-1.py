from tkinter import *

win = Tk()

mainMenu = Menu(win)
win.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as")
fileMenu.add_separator()
fileMenu.add_command(label="Close")


win.mainloop()
