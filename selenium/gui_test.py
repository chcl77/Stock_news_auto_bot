from tkinter import * 

root = Tk()
root.title("Test")
root.geometry("640x480")

listbox = Listbox(root, selectmode = "extended" , height = 0)
listbox.insert(0, "apple")
listbox.insert(END , "pear")
listbox.insert(END, "plum")
listbox.insert(END , "blossom")
listbox.pack()

root.mainloop()