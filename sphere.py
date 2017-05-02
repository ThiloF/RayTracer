import math
from point import Point
from ray import Ray
class Sphere(object):
    def __init__(self, center, radius):
        self.center = center # point
        self.radius = radius # scalar

    def __repr__(self):
        return "radius=%s, center=%s" % (self.radius,self.center)

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = co.scalarProduct(ray.direction)
        discriminant = v*v - co.scalarProduct(co) + self.radius*self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

        def normalAt(self,p):
            return (p - self.center).normalized