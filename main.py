import pattern


if __name__ == "__main__":
    resolution = 500
    tile_size = 50
    checker = pattern.Checker(resolution, tile_size)
    checker.draw()
    checker.show()
