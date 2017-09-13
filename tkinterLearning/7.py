import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

# NOTE: not necessary
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):

    # TODO: Incoming data should come from this function, so reading should be removed.
    # IDEA: It can be tested via random number generator.

    graph_data = open('/Users/mert/PycharmProjects/ECar-ABUTeam/tkinterLearning/sampleData.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    for line in lines:
        if len(line) > 1:
            xs.append(line)
    ax1.clear()
    ax1.plot(xs)

# NOTE: blit=True means only re-draw the parts that have changed.
# NOTE: interval is refreshment in miliseconds, in this case its one second


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
