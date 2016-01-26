# Vector and Point are defined in Algebra but should be in the package namespace
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
        return "Origin : {0} \n Direction : {1} \n".format(self.pos.__str__(), self.dir.__str__())

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

        return "P1 : {0} \n P2 : {1} \n P3 : {2} \n".format(self.p1.__str__(), self.p2.__str__(), self.p3.__str__())

    # def ray_intersect(self, inRay):
    #     """
    #         Ray-Triangle intersection
    #     """
    #     u = self.p2 - self.p1
    #     v = self.p3 - self.p1
    #     n = u**v
    #     if n == Vector():   # Degenerated triangle
    #         return None
    #     w0 = inRay.pos - self.p1
    #
    #
    #
    #
    #
    #     inRay.dir.CrossProduct(self.auxVec1, self.edge2)
    #     det = self.auxVec1 * self.edge1
    #     if det < EPSILON:
    #         return None
    #     self.auxVec2 = inRay.pos - self.p1
    #     u = self.auxVec2 * self.auxVec1
    #     if u < 0.0 or u > det:
    #         return None
    #
    #     self.auxVec2.CrossProduct(self.auxVec3, self.edge1)
    #     v = self.auxVec3 * inRay.dir
    #     if v < 0.0 or (u+v) > det :
    #         return None
    #     t = self.edge2 * self.auxVec3
    #     inv_det = 1.0 / det
    #     t = t * inv_det
    #     u = u * inv_det
    #     v = v * inv_det
    #
    #     return (t,u,v)
