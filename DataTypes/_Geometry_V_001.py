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

    def ray_intersect(self, inRay):
        """
            Ray-Triangle intersection
        """
        # Get the vectors from the p1 vertex to the other two
        u = self.p2 - self.p1
        v = self.p3 - self.p1
        # Calculate the geometric normal for the triangle
        normal = u**v
        # Check if it's a degenrated triangle
        if normal == Vector():   # Degenerated triangle
            return None
        # Check if ray direction and normal are perpendicular
        normal_dot_dir = normal * inRay.dir
        if mathLib.abs(normal_dot_dir) < EPSILON:    # Ray parallel to triangle
            return None 
        # Free term on the plane equation
        D = normal * self.p1.as_vector() 
        # Conpute the distance to the intersection of the ray with triangle's plane
        normal_dot_origin = normal * inRay.pos
        dist = (D - normal_dot_origin) / normal_dot_dir
        if dist < EPSILON:  # The ray is moving away
            return None
        # We get the intersection point
        iPoint = inRay.pos + inRay.dir * t
        #Create a vector from p1 to the intersection point
        w = iPoint -self.p1
        # Get the projection of this vector in the system formed by u and v
        # If any of this projections is negative or its sum  is over 1 then there 
        # is no intersection
        alpha = w * u
        if alpha < 0 :
            return None
        beta = w * v
        if (beta < 0) or ((alpha + beta) > 1):
            return None
        return (dist, alpha, beta)