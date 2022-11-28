from tkinter import *
window =Tk()
window.config(bg='grey')
fr = Frame()
def inf():
    global l1
    z = var1.get()
    if z == 1:
        l1['text'] = x1
    elif z == 2:
        l1['text'] = x2
    elif z == 3:
        l1['text'] = x3
var1 = IntVar()
var1.set(0)
r1 = Radiobutton(fr, indicatoron=0, width=10, text='Вася', variable=var1, value=1, command=inf)
r2 = Radiobutton(fr, indicatoron=0, width=10, text='Петя', variable=var1, value=2, command=inf)
r3 = Radiobutton(fr, indicatoron=0, width=10, text='Сирожа', variable=var1, value=3, command=inf)
x1 = '+7 951 456789123'
x2 = '+7 984 456789123'
x3 = '+7 456 123456789'
l1 = Label(width=20, height=10, font=20)
fr.pack(side=LEFT)
r1.pack(anchor=W)
r2.pack(anchor=W)
r3.pack(anchor=W)
l1.pack()
window.mainloop()
