from vector import Vector
class Point(object):

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other,Point):
            raise TypeError("Punkte addieren macht keinen Sinn")
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x,y,z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)

    def scalarProduct(self,other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Vector(x, y, z)


    def __repr__(self):
        return "+".join((str(self.x), str(self.y), str(self.z)))