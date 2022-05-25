import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion() #интерактивный режим

fig, ax = plt.subplots()

th = np.linspace(0, 2*np.pi, 512) #границы по оси х
ax.set_ylim(-1.5, 1.5) #границы по оси у

ln, = ax.plot(th, np.sin(th)) #построение графика

def slow_loop(N, ln):
    for j in range(N):
        time.sleep(.1)  #моделирование некоторых работ
        ln.figure.canvas.flush_events()

slow_loop(100, ln)
