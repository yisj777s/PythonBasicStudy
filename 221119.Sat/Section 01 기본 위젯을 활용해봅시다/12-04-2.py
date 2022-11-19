from tkinter import *
win=Tk()
win.title("냥이들^^")
photo=PhotoImage(file="C:/Users/user/Desktop/12장 예제 이미지/cat.gif")
photo2=PhotoImage(file="C:/Users/user/Desktop/12장 예제 이미지/cat2.gif")
label1=Label(win,image=photo)
label2=Label(win,image=photo2)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

win.mainloop()  