import numpy as np
import skimage.transform
import matplotlib.pyplot as plt
import pattern


if __name__ == "__main__":
    a = np.load("exercise_data\\1.npy")
    plt.imshow(a)
    plt.show()
    print(a.shape)
