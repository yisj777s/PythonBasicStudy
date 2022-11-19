from tkinter import *
win=Tk()

label1=Label(win, text="SWEDU~~ Python을")
label2=Label(win, text="열심히", font=("궁서체", 30), fg=("blue"))
label3=Label(win, text="공부 중입니다.", bg="magenta", width=20, height=5, anchor=NE)

label1.pack()
label2.pack()
label3.pack()

win.mainloop()