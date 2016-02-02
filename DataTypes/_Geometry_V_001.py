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
            iNormal = e1**e2
            return (dist, u, v, iPoint, iNormal, self.shade)
    def shade(self, dist, u, v, iPoint, iNormal, inDir):
        return iNormal * inDir


    def intersect_aabb(self, aabb):
        """
            Triangle-AABB intersection test
            From Real-Time Raytracing
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
            pMin.x = aabb["minX"]
            pMax.x = aabb["maxX"]
        else:
            pMax.x = aabb["minX"]
            pMin.x = aabb["maxX"]

        if normal.y >= 0:
            pMin.y = aabb["minY"]
            pMax.y = aabb["maxY"]
        else:
            pMax.y = aabb["minY"]
            pMin.y = aabb["maxY"]

        if normal.z >= 0:
            pMin.z = aabb["minZ"]
            pMax.z = aabb["maxZ"]
        else:
            pMax.z = aabb["minZ"]
            pMin.z = aabb["maxZ"]

        v_1 = pMin - p1
        v_2 = pMax - p1
        dot_1 = normal * v_1
        dot_2 = normal * v_2

        # If both points are in the same side there is not intersection
        if (dot_1*dot_2 > 0):
            return False

        # Calculate aabb center and extents
        center = Point( 0.5 * (aabb["maxX"] + aabb["minX"]),
                        0.5 * (aabb["maxY"] + aabb["minY"]),
                        0.5 * (aabb["maxZ"] + aabb["minZ"]))
        extents = Vector(   0.5 * (aabb["maxX"] - aabb["minX"]),
                            0.5 * (aabb["maxY"] - aabb["minY"]),
                            0.5 * (aabb["maxZ"] - aabb["minZ"]))
        # Move the triangle as if the aabb was at origin
        v1 = self.p1 - center
        v2 = self.p2 - center
        v3 = self.p3 - center
        # Calculate the triangle edge vectors
        f1 = v2 - v1
        f2 = v3 - v2
        f3 = v1 - v3

        # Test the axis
        # a_11
        a_11 = Vector(0.0, -f1.z, f1.y)
        p0 = v1 * a_11
        # p1 = v2 * a_11 = p0 No need to calculate
        p2 = v3 * a_11
        r = extents.y * abs(a_11.y) + extents.z * abs(a_11.z)
        if (min(p0, p2) > r or max(p0,p2) < -r) return False
        # a_12
        a_12 = Vector(0.0, -f2.z, f2.y)
        p0 = v1 * a_12
        p1 = v2 * a_12
        p2 = v3 * a_12
        r = extents.y * abs(a_12.y) + extents.z * abs(a_12.z)
        if (min(p0, p1, p2) > r or max(p0, p1, p2) < -r) return False
        # a_13
        a_13 = Vector(0.0, -f3.z, f3.y)
        p0 = v1 * a_13
        p1 = v2 * a_13
        p2 = v3 * a_13
        r = extents.y * abs(a_13.y) + extents.z * abs(a_13.z)
        if (min(p0, p1, p2) > r or max(p0, p1, p2) < -r) return False
        # a_21
        a_21 = Vector(f1.z, 0.0, -f1.x)
        p0 = v1 * a_21
        p1 = v2 * a_21
        p2 = v3 * a_21
        r = extents.x * abs(a_21.x) + extents.z * abs(a_21.z)
        if (min(p0, p1, p2) > r or max(p0, p1, p2) < -r) return False
        # a_22
        a_22 = Vector(f2.z, 0.0, -f2.x)
        p0 = v1 * a_22
        p1 = v2 * a_22
        # p2 = p1 No Need to calculate
        r = extents.x * abs(a_22.x) + extents.z * abs(a_22.z)
        if (min(p0, p1) > r or max(p0, p1) < -r) return False
        # a_23
        a_23 = Vector(f3.z, 0.0, -f3.x)
        p0 = v1 * a_23
        p1 = v2 * a_23
        p2 = v3 * a_23
        r = extents.x * abs(a_23.x) + extents.z * abs(a_23.z)
        if (min(p0, p1, p2) > r or max(p0, p1, p2) < -r) return False

        # a_31
        a_31 = Vector(-f1.y, f1.x, 0.0)
        p0 = v1 * a_31
        p1 = v2 * a_31
        p2 = v3 * a_31
        r = extents.x * abs(a_31.x) + extents.y * abs(a_31.y)
        if (min(p0, p1, p2) > r or max(p0, p1, p2) < -r) return False
        # a_32
        a_32 = Vector(-f2.y, f2.x, 0.0)
        p0 = v1 * a_32
        p1 = v2 * a_32
        p2 = v3 * a_32
        r = extents.x * abs(a_32.x) + extents.z * abs(a_32.y)
        if (min(p0, p1, p2) > r or max(p0, p1, p2) < -r) return False
        # a_33
        a_33 = Vector(-f3.y, f3.x, 0.0)
        p0 = v1 * a_33
        p1 = v2 * a_33
        # p2 = p0 No Need to calculate
        r = extents.x * abs(a_33.x) + extents.y * abs(a_33.y)
        if (min(p0, p1, p2) > r or max(p0, p1) < -r) return False

        return True
