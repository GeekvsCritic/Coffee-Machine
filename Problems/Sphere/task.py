class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        Sphere.volume = (4 / 3) * Sphere.PI * (self.radius ** 3)

