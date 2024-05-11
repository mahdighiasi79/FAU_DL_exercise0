import numpy as np
import copy
import matplotlib.pyplot as plt
from PIL import Image


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


class Circle:

    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = np.arange(resolution * resolution).reshape((resolution, resolution))

    def draw(self):
        row_numbers = np.floor(self.output / self.resolution)
        column_numbers = self.output % self.resolution
        x_distance = row_numbers - self.position[0]
        y_distance = column_numbers - self.position[1]
        position_distance = np.power(np.power(x_distance, 2) + np.power(y_distance, 2), 0.5)
        self.output = position_distance < self.radius
        self.output = np.rot90(self.output, 1, axes=(0, 1))
        return copy.deepcopy(self.output)

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()


class Spectrum:

    def __init__(self, resolution):
        self.resolution = resolution
        self.output = []

    def draw(self):
        grid = np.arange(self.resolution * self.resolution).reshape((self.resolution, self.resolution))
        x = np.floor(grid / self.resolution)
        y = grid % self.resolution

        red = np.abs(x + np.abs(y - self.resolution) - (2 * self.resolution))
        red /= (2 * self.resolution)

        green = np.abs(np.abs(x - self.resolution) + np.abs(y - (self.resolution / 2)) - (2 * self.resolution))
        green /= (2 * self.resolution)

        blue = np.abs(x + y - (2 * self.resolution))
        blue /= (2 * self.resolution)

        self.output = np.stack((red, green, blue), axis=2)
        return copy.deepcopy(self.output)

    def show(self):
        plt.imshow(self.output)
        plt.show()
