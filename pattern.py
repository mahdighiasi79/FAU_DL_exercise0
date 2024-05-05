import numpy as np
import copy
import matplotlib.pyplot as plt


class Checker:

    def __init__(self, resolution, tile_size):
        if resolution % (tile_size * 2) != 0:
            print("resolution not dividable by (2*tile_size)\n")
            return
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = np.arange(resolution * resolution, dtype=float).reshape((resolution, resolution))

    def draw(self):
        row_numbers = np.floor(self.output / self.resolution)
        column_numbers = self.output % self.resolution
        tile_row_numbers = np.floor(row_numbers / self.tile_size)
        tile_column_numbers = np.floor(column_numbers / self.tile_size)
        self.output = tile_row_numbers + tile_column_numbers
        self.output %= 2
        return copy.deepcopy(self.output)

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()
