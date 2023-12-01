class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        return

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
