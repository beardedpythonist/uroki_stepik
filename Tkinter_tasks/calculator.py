from tkinter import *

root = Tk()
e = Entry(width=20, font='arial 27')
e1 = Entry(width=20, font='arial 27')
b_plus = Button(text='+', font='arial 27')
b_plus['bg'] = '#555555'
b_minus = Button(text='-', font='arial 27')
b_umnozh = Button(text='*', font='arial 27')
b_delit = Button(text='/', font='arial 27')
l1 = Label(bg='black', fg='white', width=20, font='arial 27')
def plus(event):
    s = e.get()
    if s.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s = float(s)
        s1 = e1.get()
    if s1.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s1 = float(s1)
    total = s + s1
    l1['text'] = str(total)
b_plus.bind('<Button-1>', plus)
def minus(event):
    s = e.get()
    if s.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s = float(s)
        s1 = e1.get()
    if s1.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s1 = float(s1)
    total = s - s1
    l1['text'] = str(total)
b_minus.bind('<Button-1>', minus)
def umnozh(event):
    s = e.get()
    if s.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s = float(s)
        s1 = e1.get()
    if s1.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s1 = float(s1)
    total = s * s1
    l1['text'] = str(total)
b_umnozh.bind('<Button-1>', umnozh)
def deli(event):
    s = e.get()
    if s.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s = float(s)
        s1 = e1.get()
    if s1.isdigit() == False:
        l1['text'] = str('Ошибка')
    else:
        s1 = float(s1)
    total = s / s1
    l1['text'] = str(total)
b_delit.bind('<Button-1>',deli)

e.pack()
e1.pack()
l1.pack()
b_plus.pack(side=LEFT)
b_minus.pack(side=LEFT)
b_umnozh.pack(side=LEFT)
b_delit.pack(side=LEFT)

root.mainloop()



