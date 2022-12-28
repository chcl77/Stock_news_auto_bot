import tkinter.messagebox as msg
import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("test")
root.geometry("640x480")

def info():
    msg.showinfo("알림", "현재 정보를 알림 중입니다")

def warn():
    msg.showwarning("경고", "현재 경고를 알림 중입니다")

def error():
    msg.showerror("에러", "현재 에러를 알림 중입니다")


def okcancel():
    response = msg.askokcancel("물음", "현재 확인, 취소를 알림 중입니다")
    print(response)
    if response == 1 : 
        print("yes")
    elif response == 0 : 
        print("No")
    


Button(root , text = "알림" , command = info).pack()
Button(root , text = "경고" , command = warn).pack()
Button(root , text = "알림" , command = error).pack()
Button(root , text = "알림" , command = okcancel).pack()

root.mainloop()
