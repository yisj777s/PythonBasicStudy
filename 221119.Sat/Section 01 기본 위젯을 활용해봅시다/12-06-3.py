from tkinter import *

def myFunc():
    label1.config(text="강아지 귀엽죠?^^")

win=Tk()
photo=PhotoImage(file="C:/Users/user/Desktop/12장 예제 이미지/dog2.gif")
button1=Button(win,image=photo,command=myFunc)

label1=Label(win,text="")

button1.pack()
label1.pack()

win.mainloop()
