class Array4D:
    _arr = None

    def __init__(self, x, y, z, m):
        self._arr = [[[[""] * m] * z] * y] * x

    def get(self, x, y, z, m):
        return self._arr[x][y][z][m]

    def set(self, x, y, z,m, value):
        self._arr[x][y][z][m] = value
