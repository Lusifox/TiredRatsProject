from tkinter import *

root = Tk()
root.geometry("800x400+150+150")
root.title("Координаты")

w = Label(root, text = "Наведите на виджет, чтобы узнать координаты курсора", bg = "black")
w['fg'] = 'red'
w.config(font = ('times', 20, 'bold'))
w.config(height = 3, width = 20, bd = 8, relief = RAISED)
w.config(cursor = "cross")

def motion(event):
    x, y = event.x, event.y
    print('x = {}, y = {}'.format(x, y))

w.bind('<Motion>', motion)

w.pack(side = TOP, expand = YES, fill = BOTH)

root.mainloop()
