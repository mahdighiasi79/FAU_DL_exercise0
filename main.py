import pattern


if __name__ == "__main__":
    # resolution = 500
    # tile_size = 50
    # checker = pattern.Checker(resolution, tile_size)
    # checker.draw()
    # checker.show()

    resolution = 500
    radius = 100
    position = [200, 200]
    circle = pattern.Circle(resolution, radius, position)
    circle.draw()
    circle.show()