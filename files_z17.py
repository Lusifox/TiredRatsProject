import os

f = open('file.txt', 'w')

f.write('Hello\n')
f.write('world\n')

f.close()

if os.path.exists('file.txt'):
 print("Файл существует")
else:
 print("Файл не существует")

os.chdir(r'C:\Users\kapr2')
os.rename("file.txt", "file_nf.txt")