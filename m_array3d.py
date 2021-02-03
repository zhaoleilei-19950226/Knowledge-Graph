class Array3D:
    _arr = None

    def __init__(self, x, y, z):
        self._arr = [[[""] * z] * y] * x

    def get(self, x, y, z):
        return self._arr[x][y][z]

    def set(self, x, y, z, value):
        self._arr[x][y][z] = value
