'''#GUI
import tkinter
from tkinter import ttk

def main():
    app = tkinter.Tk() #Создаем окно
    app.title('My First App')
    app.geometry('720x480')
    app.resizable(False, False)
    app.configure(background='#CFD1D1')

  #Виджеты
    text = tkinter.Label(
    text='My first application'.upper(),
    font=('Sans-serif 35'),
    background='#CFD1D1',
  )
    text.pack()

    entry = tkinter.Entry(
    font=('Sans-serif 10'),
)
    entry.place(x=360, y=100)

    btn = ttk.Button(
    text='Press'
)
    btn.place(x=300, y=50)

    app.mainloop()     #Закрываем окно

if _name_ == 'main':
    main()
'''
import tkinter

def user():
    name = tkinter.Tk()
    name.title(Programma)
    name.geometry('200x200')
    name.resizable(False,False)
    name.configure(background='green')

    text = tkinter.Label(
        text='Hello',
        background='Red'
    )
    text.place(x=100,y=100)
    text = tkinter.Label(
        text='World',
        background='Red'
    )
    name.mainloop()
if __name__ == '__user__':
	user()
