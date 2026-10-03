from tkinter import*
tk = Tk()
tk.geometry('100x100')
tk.title('c131')
def handle_keypress(event):
    print(event.char)
tk.bind("<Key>",handle_keypress)
tk.mainloop()