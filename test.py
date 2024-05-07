import numpy as np
import pattern


if __name__ == "__main__":
    a = np.load("data.zip")
    # print(a.shape)
    print(a["Labels.json"])
