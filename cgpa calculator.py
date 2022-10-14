from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
page = Tk()
page.title('CGPA Calculator')

numb = ('1','2','3','4','5','6','7','8','9','10','11','12')
entry = []
bentry = []

def calculate():
    sob = int(set_entry.get())
    cals = sum([int(entry[x].get()) * int(bentry[y].get()) for x,y in zip(range(0,sob), range(0,sob))]) / sum([int(bentry[z].get()) for z in range(0,sob)])
    messagebox.showinfo('Your GPA', cals)
    
def put():
    for x in range(int(set_entry.get())):
        my_entry = Entry(page, width=5)
        my_entry.grid(row=x, column=0, pady=5)
        entry.append(my_entry)
        
    for y in range(int(set_entry.get())):
        entries = Entry(page, width=5)
        entries.grid(row=y, column=1, pady=5)
        bentry.append(entries)
    
Label(page, text='Grade Points', font=('arial',8,'bold')).grid(row=54, column=0, pady=10)

Label(page, text='Course Units', font=('arial',8,'bold')).grid(row=54, column=1, pady=10)

Label(page, text='Number of Course Offered :', font=('arial',8, 'bold')).grid(row=56, columnspan=2, pady=20, sticky='w')

set_entry = ttk.Combobox(page, value=numb,width=5)
set_entry.grid(row=56, column=1, pady=20, sticky='e')

Button(page,text='Ok',command=put, font=('arial',6,'bold')).grid(row=57, columnspan=2, ipadx=240, pady=5)

Button(page,text='Calculate',command=calculate, font=('arial',6,'bold')).grid(row=55, columnspan=2, pady=5, ipadx=200)

page.mainloop()