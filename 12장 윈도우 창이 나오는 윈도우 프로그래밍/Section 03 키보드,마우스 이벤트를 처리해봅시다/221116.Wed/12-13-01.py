from tkinter import *
# 함수 정의 부분


def clickLeft(event):
    label1.config(text="왼쪽 마우스를 클릭했어요.")


def clickRight(event):
    label1.config(text="오른쪽 마우스를 클릭했어요.")


# 메인 코드 부분
win = Tk()
win.title("이벤트 실습")
win.geometry("200x100")

label1 = Label(text="마우스를 클릭하세요.")
label1.pack()
win.bind("<Button-1>", clickLeft)
win.bind("<Button-3>", clickRight)

win.mainloop()
