from tkinter import *
from math import *
from tkinter.messagebox import *




root=Tk()
root.geometry("520x350")
root.title('Задание №30')
root.resizable(False, False)




def func():
    f1=ent1.get()
    f2=ent3.get()
    k=[]
    for i in range(0,11):
        if i!=1:
            k.append(0)
        else:
            k.append(1)
        

    k1=k.copy()
    k2=k.copy()
    for x in range(1,10):
        try:
            k1[eval(f1)]+=k1[x]
            k2[eval(f2)]+=k2[x]
        except IndexError:
            break
    
    g1=len(ent2.get())
    g2=len(ent4.get())
    for i in range(0,g1):
        ent2.delete(0)
    for i in range(0,g2):
        ent4.delete(0)
    for i in range(0,len(f1)):
        ent1.delete(0)
    for i in range(0,len(f2)):
        ent3.delete(0)
    ent2.insert(0,k1)
    ent4.insert(0,k2)
    
    

win2=Frame(root)
win2.pack(anchor="n", expand= YES, fill=X)
lx1=Label(win2, text="f1 = ")
lx1.pack(side=LEFT, padx=10, pady=10)

ent1=Entry(win2)
ent1.insert(0,0)
ent1.pack(side=LEFT, padx=10, pady=10)

lx2=Label(win2, text="Вывод 1 = ")
lx2.pack(side=LEFT, padx=20, pady=10)

ent2=Entry(win2)
ent2.insert(0,0)
ent2.pack(side=LEFT, padx=20, pady=10)

win3=Frame(root)
win3.pack(anchor="n", expand= YES, fill=X)
lx3=Label(win3, text="f2 = ")
lx3.pack(side=LEFT, padx=10, pady=10)

ent3=Entry(win3)
ent3.insert(0,0)
ent3.pack(side=LEFT, padx=10, pady=10)

lx4=Label(win3, text="Вывод 2 = ")
lx4.pack(side=LEFT, padx=20, pady=10)

ent4=Entry(win3)
ent4.insert(0,0)
ent4.pack(side=LEFT, padx=20, pady=10)

b=Button(root, bg="red", text="Нажмите чтобы выполнить работу функций в массиве", command=func)
b.place(x=100, y=270)


root.mainloop()




















