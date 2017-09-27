import random  # NOTE: will be deleted when random number giving is not required

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('dark_background')
fig = plt.figure()

ax1 = fig.add_subplot(1, 2, 1)  # NOTE: First
ax2 = fig.add_subplot(2, 2, 2)  # NOTE: Second
ax3 = fig.add_subplot(2, 2, 4)  # NOTE: Third

xs = []


def animate(i):
    num = random.randint(45, 500)
    # for making graph a bit smoother
    sm_num = np.array(num)
    smooth_num = np.linspace(sm_num.min(), sm_num.max(), 200)
    xs.append(smooth_num)

    if len(xs) > 10:
        del xs[0]
        # NOTE: xs should have limited amount of datum for graph to look better
    else:
        pass

    ax1.clear()
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Speed')
    ax1.plot(xs, color="red")
    ax1.grid(alpha=0.2)

    ax2.clear()
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Voltage')
    ax2.plot(xs, color="yellow")
    ax2.grid(alpha=0.2)

    ax3.clear()
    ax3.set_xlabel('ASE<3')
    ax3.set_ylabel('AtesliMertxxx')
    ax3.plot(xs, color="green")
    ax3.grid(alpha=0.2)
    fig.tight_layout()
    # plt.savefig("logs.eps") #to save figure

# NOTE: blit=True means only re-draw the parts that have changed,not required for now
# NOTE: interval is refreshment in miliseconds, in this case its one second


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
