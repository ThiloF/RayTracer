from vector import Vector
from point import Point
from ray import Ray

class Triangle(object):
    def __init__(self,a,b,c):
        self.a = a #point
        self.b = b #point
        self.c = c #point
        self.u = self.a - self.b # direction vector
        self.v = self.c - self.a # direction vector

    def __repr__(self):
        return "Triangle(%s,%s,%s)" % (repr(self.a), repr(self.b), repr(self.c))

    def intersectionParameter(self, ray):
        w = ray.origin - self.a
        dv = ray.direction.crossProduct(self.v)
        dvu = dv.scalarProduct(self.u)
        if dvu == 0.0:
            return None
        wu = w.crossProduct(self.u)
        r = dv.scalarProduct(w) / dvu
        s = wu.scalarProduct(ray.direction) / dvu
        if 0<=r and r <=1 and 0<=s and <=1 and (r+s) <= 1:
            return wu.scalarProduct(self.v) / dvu
        else:
            return None

        def normalAt(self,p):
            return self.u.crossPrdoduct(self.v).normalized()