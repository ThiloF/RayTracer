import math
from point import Point
from ray import Ray
class Sphere(object):
    def __init__(self, center, radius,color):
        self.center = center # point
        self.radius = radius # scalar
        self.color = color

    def __repr__(self):
        return "radius=%s, center=%s" % (self.radius,self.center)

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = co * ray.direction
        discriminant = v*v - co * co + self.radius*self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self,p):
        return (p - self.center).normalized

    def colorAt(self, ray):
        return self.color