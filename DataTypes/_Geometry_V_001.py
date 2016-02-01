import math as mathLib
from .PR_CONSTANTS import EPSILON

from ._Algebra_V_001 import Vec3 as Vector, Point3 as Point

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

    def aabb_intersect(self, aabb):
        """
            Triangle-AABB intersection test
        """
        # Check for aabb collision
        maxX = max(self.p1.x,self.p2.x,self.p3.x)
        if aabb["maxX"] < minX return False
        minX = min(self.p1.x,self.p2.x,self.p3.x)
        if aabb["minX"] > maxX return False
        maxY = max(self.p1.y,self.p2.y,self.p3.y)
        if aabb["maxY"] < minY return False
        minY = min(self.p1.y,self.p2.y,self.p3.y)
        if aabb["minY"] > maxY return False
        maxZ = max(self.p1.z,self.p2.z,self.p3.z)
        if aabb["maxZ"] < minZ return False
        minZ = min(self.p1.z,self.p2.z,self.p3.z)            
        if aabb["minZ"] > maxZ return False

        # We check if the triangle plane intersects the aabb
        e1 = self.p2 - self.p1
        e2 = self.p3 - self.P1
        normal = e1**e2
        pMin = Point()
        pMax = Point()

        # We generate two point in a way that the vector between them gets the highest possible dot product with the normal
        if normal.x >= 0:
            vMin.x = aabb["minX"]
            vMax.x = aabb["maxX"]
        else:
            vMax.x = aabb["minX"]
            vMin.x = aabb["maxX"]

        if normal.y >= 0:
            vMin.y = aabb["minY"]
            vMax.y = aabb["maxY"]
        else:
            vMax.y = aabb["minY"]
            vMin.y = aabb["maxY"]

        if normal.z >= 0:
            vMin.z = aabb["minZ"]
            vMax.z = aabb["maxZ"]
        else:
            vMax.z = aabb["minZ"]
            vMin.z = aabb["maxZ"]

        v_1 = pMin - p1
        v_2 = pMax - p1
        dot_1 = normal * v_1
        dot_2 = normal * v_2

        # If both points are in the same side there is not intersection
        if (dot_1*dot_2 > 0):
            return False



        return True

        { "maxX":-INF,"minX":INF,
                    "maxY":-INF,"minY":INF,
                    "maxZ":-INF,"minZ":INF }
