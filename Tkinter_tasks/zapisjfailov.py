from tkinter import *

root = Tk()
fr_top = Frame(root)
fr_bot = Frame(root)


e = Entry(fr_top,  width=20, font='arial 20')
b1 = Button(fr_top, text='открыть', width=30)
b2 = Button(fr_top, text='сохранить', width=30)

tx = Text(fr_bot, width=60, height= 6, font='arial 15')

scroll = Scrollbar(command=tx.yview)
scroll.pack(side=LEFT, fill=Y)

tx.config(yscrollcommand=scroll.set)


def otr():
    tx.delete(1.0, END)
    x = e.get()
    for c in open(x):
        tx.insert(1.0, c)
b1.config(command=otr)

def zapis():
    x = e.get()
    funk_file = open(x, 'w')
    read_text = tx.get('1.0', END)
    funk_file.write(read_text)
    funk_file.close()
b2.config(command=zapis)

fr_top.pack()
fr_bot.pack()
e.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
tx.pack()

mainloop()

