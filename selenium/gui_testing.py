from tkinter import * 

root = Tk()
root.title("stock_crawling")
root.geometry("640x480")


def pso() :
    global label1
    label1 = Label(root, text = "hello world")
    label1.pack()

def pso2() :
    label1.config(text = "hello commander")
     

def clear():
    print(ent.get())
    global names 
    names = ent.get()
    ent.delete(0, END)
    
btn = Button(root, text = "button", command = pso)
btn.pack()
# btn2 = Button(root, text = "button", command = pso2)
# btn2.pack()
label1 = Label(root, text = "주식 크롤링 프로그램")
label1.pack()
label1.place(x=265, y = 10)
btn3 = Button(root, text = "시작" , width= 10 , command = clear)

btn3.pack()
btn3.place(x=540, y=95)

# txt = Text(root , width = 50)
# txt.pack()
ent = Entry(root , width = 70)
ent.pack()
ent.place(x=10, y=100)
ent.insert(END,  "입력하십시오")

root.mainloop()