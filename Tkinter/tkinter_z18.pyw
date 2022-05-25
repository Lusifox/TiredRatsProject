from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor

root = Tk()
root.title("Главное окно программы")
root.geometry("300x300+250+250")

win1 = Frame(root, bg = '#555555')

win1.pack(anchor = "n", expand = "YES", fill = X)

def closeQuery():

    if askyesno('Выход из программы...', 'Закрыть программу?'):
        showwarning('Диалоговое окно', 'Внимание выход из программы!')
        root.destroy()
    else:
        showinfo('Диалоговое окно', 'Вы решили остаться в программе')

Button(win1, text = 'Выход', command = closeQuery).pack(side = RIGHT, padx = 10, pady = 5)

def Ghoul(w):

    showinfo('Правильно', 'Может по чашечке кофе в Антэйку?')

def notGhoul(w):

    showinfo('Не верно', 'Всё с тобой понятно.')

def newWindow():
    topL1 = Toplevel(root)
    topL1.title("Проверка на интелектуальность")
    topL1.transient(root)
    topL1.geometry("200x200+250+250")

    b1 = Button(topL1, text = 'Я - Гуль', command  = (lambda:Ghoul(b1)), fg = 'blue')
    b2 = Button(topL1, text = '993', command  = (lambda:notGhoul(b2)), fg = 'red')
    b1.pack()
    b2.pack()

Button(win1, text = "1000-7?", command = newWindow).pack(side = RIGHT, padx = 10, pady = 5)

root.mainloop()