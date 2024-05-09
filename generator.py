import math
import os.path
import json
import random
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
import skimage

num_images = 100


# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the label dictionary.

        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}

        #TODO: implement constructor
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        self.batch_number = 0
        self.num_epoch = 0

    def add_image(self, i, images, labels, labels_dict):
        img = np.load(self.file_path + str(i) + ".npy")
        img = self.augment(img)
        img = skimage.transform.resize(img, self.image_size)
        images.append(img)
        labels.append(labels_dict[str(i)])

    def next(self):
        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
        images = []
        labels = []
        labels_dict = open(self.label_path)
        labels_dict = json.load(labels_dict)
        num_batches = np.floor(num_images / self.batch_size)
        batch_start = self.batch_number * self.batch_size

        data_order = np.arange(num_images)
        if self.shuffle:
            np.random.shuffle(data_order)

        if self.batch_number >= num_batches:
            self.num_epoch += 1
            for i in range(batch_start, num_images):
                self.add_image(data_order[i], images, labels, labels_dict)
            for i in range(self.batch_size - (num_images - batch_start)):
                self.add_image(data_order[i], images, labels, labels_dict)
            if batch_start == num_images:
                self.batch_number = 1
            else:
                self.batch_number = 0

        else:
            batch_end = (self.batch_number + 1) * self.batch_size
            for i in range(batch_start, batch_end):
                self.add_image(data_order[i], images, labels, labels_dict)
            self.batch_number += 1

        images = np.array(images)
        labels = np.array(labels)
        return images, labels

    def augment(self, img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function

        if self.mirroring:
            y_n = random.randint(0, 1000) % 2
            if y_n == 1:
                img = np.fliplr(img)

        if self.rotation:
            degree = random.randint(0, 5000) % 4
            img = np.rot90(img, degree, axes=(1, 0))

        return img

    def current_epoch(self):
        # return the current epoch number
        return self.num_epoch

    def class_name(self, x):
        # This function returns the class name for a specific input
        #TODO: implement class name function
        return self.class_dict[x]

    @staticmethod
    def divisors_generator(x):
        result = []
        for i in range(1, x + 1):
            if x % i == 0:
                result.append(i)
        return result

    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        #TODO: implement show method
        divisors = self.divisors_generator(self.batch_size)
        middle = math.floor(len(divisors) / 2)
        num_cols = divisors[middle]
        if len(divisors) % 2 == 0:
            num_rows = divisors[middle + 1]
        else:
            num_rows = num_cols

        images, labels = self.next()
        f, axarr = plt.subplots(num_rows, num_cols, constrained_layout=True)
        for i in range(num_rows):
            for j in range(num_cols):
                axarr[i, j].imshow(images[(i * num_cols) + j])
                axarr[i, j].set_title(self.class_dict[labels[(i * num_cols) + j]])
        plt.show()
