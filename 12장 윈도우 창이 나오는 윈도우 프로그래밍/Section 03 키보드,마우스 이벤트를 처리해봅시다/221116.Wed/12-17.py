from tkinter import *
from time import *
# 변수 선언 부분
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif",
             "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None]*9
num = 0

# 함수 선언 부분


def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file="C:/12장 실습 예제 이미지/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:/12장 실습 예제 이미지/"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


def pageUp(event):
    clickNext()


def pageDown(event):
    clickPrev()


# 메인 코드 부분
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")
window.bind("<Prior>", pageUp)
window.bind("<Next>", pageDown)

btnPrev = Button(window, text="<<이전", command=clickPrev)
btnNext = Button(window, text="다음>>", command=clickNext)

photo = PhotoImage(file="C:/12장 실습 예제 이미지/"+fnameList[0])
pLabel = Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
