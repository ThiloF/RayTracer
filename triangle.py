from vector import Vector
from point import Point
from ray import Ray

class Triangle(object):
    def __init__(self,a,b,c,color):
        self.a = a #point
        self.b = b #point
        self.c = c #point
        self.u = self.b - self.a # direction vector
        self.v = self.c - self.a # direction vector
        self.color = color

    def __repr__(self):
        return "Triangle(%s,%s,%s)" % (repr(self.a), repr(self.b), repr(self.c))

    def intersectionParameter(self, ray):
        w = ray.origin - self.a
        dv = ray.direction.crossProduct(self.v)
        dvu = dv * self.u
        if dvu == 0.0:
            return None
        wu = w.crossProduct(self.u)
        r = dv * w / dvu
        s = wu * ray.direction / dvu
        if (0<=r) and (r <=1) and (0<=s) and (s<=1) and (r+s) <= 1:
            return wu * self.v / dvu
        else:
            return None

    def normalAt(self,p):
        return self.u.crossPrdoduct(self.v).normalized()

    def colorAt(self, ray):
        return self.color