class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
