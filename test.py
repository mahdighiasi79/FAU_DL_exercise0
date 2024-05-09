import copy
import math
import numpy as np
import skimage.transform
import matplotlib.pyplot as plt
import pattern


if __name__ == "__main__":
    b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(b)
    print("////////////////")
    b.transpose()
    print(b)

    # a = np.load("exercise_data\\1.npy")
    # print(a.shape)
    # a.transpose()
    # print(a.shape)
    # plt.imshow(a)
    # plt.show()
    # mirror(a)
    # plt.imshow(a)
    # plt.show()
    # print(a.shape)
