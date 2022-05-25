import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0., 8., 0.2)


plt.plot(t, t, 'd--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()

"-----------------------------------------------------------------------------------------------------------"

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

"-----------------------------------------------------------------------------------------------------------"

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'd', t2, f(t2), 'g')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'g--')
plt.show()

"-----------------------------------------------------------------------------------------------------------"

mu, sigma = 150, 18
x = mu + sigma * np.random.randn(10000)


n, bins, patches = plt.hist(x, 50, density=1, facecolor='r', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=150,\ \sigma=18$')
plt.axis([40, 250, 0, 0.03])
plt.grid(True)
plt.show()

"-----------------------------------------------------------------------------------------------------------"


fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=0.5)

dt = 0.01
t = np.arange(0, 30, dt)


np.random.seed(19680801)


nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt
cnse2 = np.convolve(nse2, r, mode='same') * dt


s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

ax1.plot(t, s1, t, s2)
ax1.set_xlim(0, 5)
ax1.set_xlabel('time')
ax1.set_ylabel('s1 and s2')
ax1.grid(True)

cxy, f = ax2.csd(s1, s2, 256, 1. / dt)
ax2.set_ylabel('CSD (db)')
plt.show()