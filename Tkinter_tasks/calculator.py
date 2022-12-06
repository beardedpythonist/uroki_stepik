from tkinter import *

window = Tk()
window.title('Чудо-машина')
window.geometry('500x580+450+50')
window.resizable(False, False)
window.config(bg='#BC8F8F')

# создание окна вывода результата
formula = 0
lbl = Label(text=formula, font=('Roboto', 30, 'bold'), bg='#BC8F8F')
lbl.place(x=11, y=50)


def calc(y):
    global formula
    if y == 'C':
        formula = ''
    elif y == 'del':
        formula = formula[0:-1]
    elif y == 'x ^ 2':
        formula = str(eval(formula) ** 2)
    elif y == '=':
        formula = str(eval(formula))
    elif y == '+/-':
        formula = str(eval(formula) * -1)
    else:
        if formula == 0:
            formula = ''
        formula += y
    lbl.configure(text=formula)


# создаем кнопки
buttons = ['C', 'del', '+', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '+/-', '0', '%', 'x ^ 2']
x = 18
y = 140

# разбмещаем и подписываем кнопки  и связываем с фунцией
for button in buttons:
    get_lbl = lambda x=button: calc(x)
    Button(text=button, bg='#EEE8AA', font=('Roboto, 20'), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81
window.mainloop()

