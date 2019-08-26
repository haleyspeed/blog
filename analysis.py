import ioclass

intensity = [0, 50, 100, 150, 200, 250, 300, 350]
slope = [0.00881, 0.27161, 0.11727, 0.15019, 0.21035, 0.27902, 0.3418, 0.35618]

fig, ax = plt.subplots(figsize=(4,4), dpi = 100)

exp3 = ioclass.iocurve (fig, ax, intensity, slope)

exp3.ax.spines['top'].set_visible(False)
exp3.ax.spines['right'].set_visible(False)
exp3.ax.set_xlabel(exp.x_title, size = 12)
exp3.ax.set_ylabel(exp.y_title, size = 12)