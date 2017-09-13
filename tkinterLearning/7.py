import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('/Users/mert/PycharmProjects/ElectricCarProject-AIU-GUI/???"18/tkinterLearning/sampleData.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plıt(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
