#!/usr/bin/python
from PIL import Image
from vector import Vector
from ray import Ray
from point import Point
import math

HEIGHT = 400
WIDTH = 400
objectlist = []
BACKGROUND_COLOR = (255,255,255)
img = Image.new('RGB',(WIDTH,HEIGHT))

def rayCast():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            ray = calcRay(x,y)
            maxdist = float('inf')
            color = BACKGROUND_COLOR
            for object in objectlist:
                hitdist = object.intersectionParameter(ray)
                if hitdist < maxdist:
                    maxdist = hitdist
                    color = object.colorAt(ray)
            img.putpixel((x,y), color)

def saveAsPNG():
    img = Image.new('RGB',(WIDTH,HEIGHT))

    for x in range(HEIGHT):
        for y in range(WIDTH):
            img.putpixel((x,y),(255,0,0))

    img.save("test.png")

if __name__ == "__main__":
    v = Vector(2,3,4)
    w = Vector(2,2,2)
    n = v + w
    ray = Ray(Point(0,0,0), Vector(10,0,0))
    print(ray.pointAtParameter(10))


