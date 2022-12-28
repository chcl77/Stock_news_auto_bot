import time
import tkinter.ttk as ttk
from tkinter import * 

root = Tk()
root.title("test")
root.geometry("640x480")


p_var = DoubleVar()
progressbar = ttk.Progressbar(root , maximum = 100 , length = 200 , variable = p_var)
progressbar.pack()

def cse() : 
    for i in  range(1, 101): 
        time.sleep(0.01)
        p_var.set(i)
        progressbar.update()

btn = Button(root , text = "click" , command = cse)
btn.pack()

root.mainloop()
