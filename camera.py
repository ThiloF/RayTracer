from vector import Vector
from ray import Ray
from point import Point
from sphere import Sphere
from PIL import Image

class Camera(object):
    def __init__(self, objectlist,width, height, image):
        self.objectlist = objectlist
        self.width = width
        self.height = height
        self.image = image
        self.c = Vector(0,0,0)
        self.e = Vector(0,0,0)
        self.up = Vector(0,0,0)
        self.f = self.calcF(self.c,self.e)
        self.s = self.calcF(self.f, self.up)
        self.u = self.calcU(self.s, self.f)

    def run(self):
        for x in range(self.width):
            for y in range(self.height):
                ray = self.calcRay(x,y)
                maxdist = float('inf')
                color = (255,0,0)
                for o in self.objectlist:
                    hitdist = o.intersectionParameter(ray)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            color = o.colorAt(ray)
                self.image.putPixel((x,y), color)


    def calcRay(self,x,y):
        xcomp = self.s.scale(x * self.width - self.width / 2)
        ycomp = self.u.scale(y * self.height - self.height / 2)
        return Ray(self.e, self.f + xcomp + ycomp)

    def calcF(self, c, e):
        return (c - e) / (c - e).length()

    def calcS(self, f, up):
        return f.crossProduct(up) / f.crossProduct(up).length()

    def calcU(self,s,f):
        return s.crossProduct(f)


