from tkinter import *
from tkinter import messagebox
# 함수 정의 부분


def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")


# 메인 코드 보분
window = Tk()

photo = PhotoImage(file="C:/Users/user/Desktop/12장 예제 이미지/dog.gif")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()