from tkinter import*
from tkinter import messagebox
tk= Tk()
tk.geometry("200x200")
def msg():
    messagebox.showwarning("Alert","virus found")
    messagebox.showinfo("Alert","restart your system")
button = Button(tk,text = "scan for virus",command = msg)
button.place(x=60,y = 60)
tk.mainloop()