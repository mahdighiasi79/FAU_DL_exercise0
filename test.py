import copy
import json
import math
import random
from PIL import Image
import numpy as np
import skimage.transform
import matplotlib.pyplot as plt
import pattern


def divisors_generator(x):
    result = []
    for i in range(1, x + 1):
        if x % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    print(divisors_generator(12))
