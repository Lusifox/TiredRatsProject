from tkinter import *




def poisk():
    
    a=vvod.get()
    for i in range(0,len(a)):
        vvod.delete(0)
        vivod.delete(0)
    s=a.split()
    i=100000000
    k=0
    for j in s:
        if (i>=len(j)):
            i=len(j)
            k=j
    
        
    vivod.insert(0,k)

        
        
    
    

root=Tk()
root.geometry("520x520")
root.title('Задание  №13')
root.resizable(False, False)
v=Label(root, text="Ввод")
v.place(x=100, y=80)
vvod=Entry(root, width =50 )

vvod.place(x=100, y=100)
vi=Label(root, text="Вывод")
vi.place(x=100, y=180)
vivod=Entry(root, width=50)

vivod.place(x=100, y=200)

b=Button(root, bg="red", text=" Нажмите чтобы найти наибольшее по длине слово ", command=poisk)
b.place(x=100, y=300)


root.mainloop()

