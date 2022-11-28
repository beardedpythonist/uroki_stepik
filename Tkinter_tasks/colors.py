from tkinter import *

root = Tk()

l = Label(width=30, font=' arial 27')
e1 = Entry(width=10, font=' arial 20', justify=CENTER)
b_kr = Button(width=30, bg='#ff0000')
b_orang = Button(width=30, bg='#ff7d00')
b_zhelt = Button(width=30, bg='#ffff00')
b_sel = Button(width=30, bg='#00ff00')
b_gol = Button(width=30, bg='#007dff')
b_sin = Button(width=30, bg='#0000ff')
b_fiol = Button(width=30, bg='#7d00ff')
def krasn():
    e1.delete(0, END)
    l['text'] = 'красный'
    e1.insert(0, '#ff0000')
b_kr.config(command=krasn)
def oran():
    e1.delete(0, END)
    l['text'] = 'оранжевый'
    e1.insert(0, '#ff7d00')
b_orang.config(command=oran)
def zhelt():
    e1.delete(0, END)
    l['text'] = 'желтый'
    e1.insert(0, '#ffff00')
b_zhelt.config(command=zhelt)
def sel():
    e1.delete(0, END)
    l['text'] = 'зеленый'
    e1.insert(0,'#00ff00')
b_sel.config(command=sel)
def golu():
    e1.delete(0, END)
    l['text'] = 'голубой'
    e1.insert(0,'#007dff')
b_gol.config(command=golu)
def sini():
    e1.delete(0, END)
    l['text'] = 'синий'
    e1.insert(0,'#0000ff')
b_sin.config(command=sini)
def fiol():
    e1.delete(0, END)
    l['text'] = 'фиол'
    e1.insert(0,'#7d00ff')
b_fiol.config(command=fiol)
l.pack()
e1.pack()
b_kr.pack()
b_orang.pack()
b_zhelt.pack()
b_sel.pack()
b_gol.pack()
b_sin.pack()
b_fiol.pack()

root.mainloop()
