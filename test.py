import numpy as np
import pattern


if __name__ == "__main__":
    # a = np.arange(3, dtype=float)
    # print(a)
    checker = pattern.Checker(8, 4)
    print(checker.draw())
