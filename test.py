import numpy as np
import skimage.transform
import matplotlib.pyplot as plt
import pattern


if __name__ == "__main__":
    img = np.load("exercise_data\\1.npy")
    plt.imshow(img)
    plt.show()
    img = skimage.transform.resize(img, [100, 100, 3])
    plt.imshow(img)
    plt.show()
