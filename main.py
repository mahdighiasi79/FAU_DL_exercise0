import pattern
import generator


if __name__ == "__main__":
    gen = generator.ImageGenerator("exercise_data\\", "Labels.json", 15, [100, 100, 3], True, True, True)
    gen.show()

    resolution = 1000
    tile_size = 50
    checker = pattern.Checker(resolution, tile_size)
    checker.draw()
    checker.show()

    resolution = 1000
    radius = 100
    position = [300, 300]
    circle = pattern.Circle(resolution, radius, position)
    circle.draw()
    circle.show()

    resolution = 1000
    spectrum = pattern.Spectrum(resolution)
    spectrum.draw()
    spectrum.show()
