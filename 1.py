import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

x = np.linspace(-5,5,100)
y = 10*x**3 + 650

fig, ax = plt.subplots()

ax.plot(x,y, color = 'green', lw = 5)
ax.vlines(0, y.min(), y.max(),color = 'red',lw = 3)
ax.hlines(0, x.min(), x.max(),color = 'yellow',lw = 3)

fig.set_figwidth(4); fig.set_figheight(8)

plt.show()