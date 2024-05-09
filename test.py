import copy
import json
import math
import random
from PIL import Image
import numpy as np
import skimage.transform
import matplotlib.pyplot as plt
import pattern


class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}


if __name__ == "__main__":
    images = []
    for i in range(4):
        images.append(np.load("exercise_data\\" + str(i) + ".npy"))
    images = np.array(images)

    labels = []
    dictionary = open("Labels.json")
    dictionary = json.load(dictionary)
    for i in range(4):
        labels.append(class_dict[int(dictionary[str(i)])])

    f, axarr = plt.subplots(2, 2, constrained_layout=True)
    axarr[0, 0].imshow(images[0])
    axarr[0, 1].imshow(images[1])
    axarr[1, 0].imshow(images[2])
    axarr[1, 1].imshow(images[3])
    axarr[0, 0].set_title(labels[0])
    axarr[0, 1].set_title(labels[1])
    axarr[1, 0].set_title(labels[2])
    axarr[1, 1].set_title(labels[3])
    plt.show()
