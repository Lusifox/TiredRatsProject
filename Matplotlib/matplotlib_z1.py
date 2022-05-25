import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200) #задаем ось х
y = np.cos(x) #задаем ось у

fig, ax = plt.subplots()
ln, = ax.plot(x, y) #построение графика
ln.set_color('orange') #изменение цвета
plt.show() #отображение графика

