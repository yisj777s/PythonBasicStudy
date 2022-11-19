from tkinter import *
win=Tk()

btnList=[None]*3

for i in range(0,3):
    btnList[i]=Button(win,text="버튼"+str(i+1))
    btnList[i].pack(fill=X, padx=10,pady=10,ipadx=10,ipady=10)

win.mainloop()