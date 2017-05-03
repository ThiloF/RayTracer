import math

class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def normalized(self):
        if self.length() == 0:
            return 0
        k = 1.0 / self.length() #kehrwert
        return self.scale(k)

    def scale(self,t):
        return Vector(self.x * t, self.y * t, self.z * t)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x + y + z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x,y,z)

    def __repr__(self):
        return "+".join((str(self.x),str(self.y),str(self.z)))

    def crossProduct(self,direction):
        x = self.y * direction.z - direction.y * self.z
        y = self.z * direction.x - direction.z * self.x
        z = self.x * direction.y - direction.x * self.y
        return Vector(x,y,z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)