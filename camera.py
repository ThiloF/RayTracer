from vector import Vector
from ray import Ray
from point import Point
from sphere import Sphere
from PIL import Image
import math

class Camera(object):
    def __init__(self, objectlist,image, imageHeight, imageWidth, fov):
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.objectlist = objectlist
        self.image = image
        self.c = Vector(0,3,0)
        self.e = Vector(0,1.8,10)
        self.up = Vector(0,-1,0)
        self.f = (self.c - self.e).normalized()
        self.s = self.f.crossProduct(self.up).normalized()
        self.u = self.s.crossProduct(self.f)

        self.alpha = fov / 2
        self.aspectratio = imageWidth / imageHeight
        print(self.aspectratio)
        self.height = 2 * math.tan(self.alpha * math.pi / 180.0)
        self.width = self.aspectratio * self.height

        self.pixelWidth = self.width / (imageWidth - 1)
        self.pixelHeight = self.height / (imageHeight - 1)

    def run(self):
        print("moin")
        for x in range(self.imageWidth):
            for y in range(self.imageHeight):
                ray = self.calcRay(x,y)
                #print(ray.origin, ray.direction)
                maxdist = float('inf')
                color = (255,255,255)

                for o in self.objectlist:
                    hitdist = o.intersectionParameter(ray)
                    #print(hitdist)
                    if hitdist:
                        if hitdist < maxdist:
                            maxdist = hitdist
                            color = o.colorAt(ray)
                            #print(color)
                self.image.putpixel((x,y), color)
        return self.image


    def calcRay(self,x,y):
        #x - self.width / 2 zentriert das Bild
        # /self.width skaliert das Bild auf die Kamera
        xcomp = self.s.scale(x * self.pixelWidth - self.width / 2)
        ycomp = self.u.scale(y * self.pixelHeight - self.height / 2)
        return Ray(self.e, self.f + xcomp + ycomp)



