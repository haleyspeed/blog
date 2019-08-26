import matplotlib.pyplot as plt

class iocurve ():
    def __init__(self, fig, ax, x, y):
        self.x = x
        self.y = y
        self.colors = 'blue'
        self.ax = ax
        self.ax.scatter (x, y, color = self.colors)
        self.x_title = 'Intensity (mA)'
        self.y_title = 'Slope (mV)'