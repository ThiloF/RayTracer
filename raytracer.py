#!/usr/bin/python
from PIL import Image
from vector import Vector
from ray import Ray
from point import Point
from sphere import Sphere
from triangle import Triangle
import math
from camera import Camera

HEIGHT = 400
WIDTH = 400
objectlist = []
BACKGROUND_COLOR = (255,255,255)
img = Image.new('RGB',(WIDTH,HEIGHT))


if __name__ == "__main__":

    sphere1 = Sphere(Vector(2.5,3,-10), 2, (255,0,0))
    sphere2 = Sphere(Vector(0, 7, -10), 2, (0, 0, 255))
    sphere3 = Sphere(Vector(-2.5, 3, -10), 2, (0, 255, 0))

    trangle = Triangle(Point(-2.5,3,-11),Point(0,7,-11),Point(2.5,3,-11),(0,0,255))

    img = Image.new('RGB', (WIDTH, HEIGHT))

    camera = Camera([sphere1,sphere2,sphere3,trangle],img,WIDTH, HEIGHT, 45.0)

    ray = Ray(Vector(0,0,-10), Vector(0,0.05,1))
    print(sphere1.intersectionParameter(ray))
    img = camera.run()
    img.save("test.png")
    img.show()

