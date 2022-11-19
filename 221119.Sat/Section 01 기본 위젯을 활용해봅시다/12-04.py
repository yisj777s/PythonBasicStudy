from tkinter import *
win=Tk()

photo=PhotoImage(file="C:/Users/user/Desktop/12장 예제 이미지/dog.gif")
label1=Label(win,image=photo)

label1.pack()

win.mainloop()