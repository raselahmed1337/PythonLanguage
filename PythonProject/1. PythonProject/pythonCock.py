from tkinter import *
from time import strftime

root=Tk()
root.title('Clock')

def time():
    string = strftime('%H : %M : %S %p')
    Label.config(text=string)
    Label.after(1000,time)


Label=Label(root,font=('arial',40,'bold'), background='white',foreground='black')
Label.pack(anchor='center')
time()
mainloop()
