from tkinter import *

windows = Tk()
windows.title('New_Window')
windows.geometry('420x320')
windows.configure(background='black')
list = Listbox( width=20)
list.place(x=20, y=20 )
entry = Entry(text = 'add' )
entry.place(x=150, y=20)
windows.mainloop()