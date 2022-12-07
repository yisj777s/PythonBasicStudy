from tkinter import *


def fileOpen():
    label1.config(text="파일 열기")


def fileSave():
    label1.config(text="파일 저장")


def fileSaveAs():
    label1.config(text="다른 이름으로 파일 저장")


def fileClose():
    win.quit()


def editCopy():
    label1.config(text="복사하기")


def editCut():
    label1.config(text="잘라넣기")


def editPaste():
    label1.config(text="붙여넣기")


def editSelectAll():
    label1.config(text="모두 선택")


win = Tk()
win.title("메뉴 만들기")
win.geometry("400x100")

mainMenu = Menu(win)
win.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=fileOpen)
fileMenu.add_command(label="Save", command=fileSave)
fileMenu.add_command(label="Save as", command=fileSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=fileClose)


editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="copy", command=editCopy)
editMenu.add_command(label="cut", command=editCut)
editMenu.add_command(label="paste", command=editPaste)
editMenu.add_separator()
editMenu.add_command(label="SelectAll", command=editSelectAll)

label1 = Label(win, text="")
label1.pack()

win.mainloop()
