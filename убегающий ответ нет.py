from tkinter import*
from tkinter import messagebox
import random
def no():
    messagebox.showinfo(' ',  'Я знаю')
    quit()
def motionMouse(event):
    btnn.place(x=random.randint(100, 500), y=random.randint(100, 300))
root = Tk()
root.geometry('613x409')



x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.title(' ')
root.resizable(width=False, height=False)
root['bg'] = 'white'
label = Label(root, text='ти знаешь матиматику ', font='Arial 40 bold', bg = 'white').pack()
btnn = Button(root, text='Да', font='Arial 40 bold')
btnn.place(x=170, y=100)
btnn.bind('<Enter>', motionMouse)
btny = Button(root, text='Нет', font='Arial 40 bold', command=no).place(x=350, y=100)
root.mainloop()
