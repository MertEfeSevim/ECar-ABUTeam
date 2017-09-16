import random  # NOTE: will be deleted when random number giving is not required

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use('dark_background')

fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)  # NOTE: First
ax2 = fig.add_subplot(2, 2, 2)  # NOTE: Second
ax3 = fig.add_subplot(2, 2, 4)  # NOTE: Third


xs = []


def animate(i):
    num = random.randint(45, 500)
    xs.append(num)

    if len(xs) > 20:
        del xs[0]
        # NOTE: xs should have limited amount of datum for graph to look better
    else:
        pass

    ax1.clear()
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Speed')
    ax1.plot(xs)

    ax2.clear()
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Voltage')
    ax2.plot(xs)

    ax3.clear()
    ax3.set_xlabel('ycy<3')
    ax3.set_ylabel('Ycynin aq')
    ax3.plot(xs)

# NOTE: blit=True means only re-draw the parts that have changed,not required for now
# NOTE: interval is refreshment in miliseconds, in this case its one second


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.grid(True)

plt.show()
