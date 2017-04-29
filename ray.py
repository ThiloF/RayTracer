from vector import Vector

class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin # p o i n t
        self.direction = direction.normalized() #v e c t o r

    def __repr__(self):
        return "Ray(%s ,% s )" % (repr(self.origin) , repr(self.direction))

    def pointAtParameter(self, t) :
        return self.origin + self.direction.scale(t)
