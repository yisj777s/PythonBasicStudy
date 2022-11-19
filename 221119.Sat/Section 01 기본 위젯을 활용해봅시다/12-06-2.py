from tkinter import *

def myFunc():
    #button1.destroy()
    label1=Label(text="강아지가 귀엽죠?^^")
    label1.pack()   

win=Tk()
photo=PhotoImage(file="C:/Users/user/Desktop/12장 예제 이미지/dog2.gif")
button1=Button(win,image=photo,command=myFunc)

button1.pack()

win.mainloop()
