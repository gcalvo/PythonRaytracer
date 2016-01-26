import math as mathLib

from ._Algebra_V_001 import Vec3 as Vector, Point3 as Point
EPSILON = 0.000001

class RayA():
    """
        Ray class definition
    """
    def __init__(self, origin=Point(x=0.0,y=0.0,z=0.0), direction=Vector(x=0.0,y=-1.0,z=0.0)):
        self.pos = origin
        self.dir = direction

    def __str__(self):
        return "Origin : {0} \nDirection : {1} \n".format(self.pos.__str__(), self.dir.__str__())

class TriangleA():
    """
        Triangle class definition
    """
    Epsilon = 0.000001
    def __init__(self, p1=Point(x=1.0,y=0.0,z=0.0), p2=Point(x=0.0,y=1.0,z=0.0), p3=Point(x=0.0,y=0.0,z=1.0)):

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):

        return "P1 : {0} \nP2 : {1} \nP3 : {2} \n".format(self.p1.__str__(), self.p2.__str__(), self.p3.__str__())

    def ray_intersect(self, inRay):
        """
            Ray-Triangle intersection
        """
        # Get the vectors from the p1 vertex to the other two
        e1 = self.p2 - self.p1
        e2 = self.p3 - self.p1

        P = inRay.dir**e2
        det = P * e1
        if (det > -EPSILON and det < EPSILON):
            return None
        inv_det = 1.0 / det

        T = inRay.pos - self.p1
        u = (T * P) * inv_det

        if (u < 0 or u > 1.0):
            return None

        Q = T**e1
        v = (inRay.dir * e1) * inv_det

        if (v < 0 or (v + u) > 1.0):
            return None

        dist = (e2 * Q) * inv_det

        if dist > EPSILON :
            iPoint = (inRay.pos.as_vector() + inRay.dir * dist).as_point()
            return (dist, u, v, iPoint)
