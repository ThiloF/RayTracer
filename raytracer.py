#!/usr/bin/python
from PIL import Image
from vector import Vector
from ray import Ray
from point import Point
from sphere import Sphere
import math
from camera import Camera

HEIGHT = 400
WIDTH = 400
objectlist = []
BACKGROUND_COLOR = (255,255,255)
img = Image.new('RGB',(WIDTH,HEIGHT))


if __name__ == "__main__":
    sphere = Sphere(Vector(0,0,0), 1, (255,0,0))
    img = Image.new('RGB', (WIDTH, HEIGHT))
    camera = Camera([sphere,], WIDTH, HEIGHT, img)
    sphere1 = Sphere(Vector(0,0,0), 1, (255,0,0))
    ray = Ray(Vector(0,0,-10), Vector(0,0.05,1))
    print(sphere1.intersectionParameter(ray))
    img = camera.run()
    img.save("test.png")
    img.show()

