#!/usr/bin/python
# -*- encoding: utf-8 -*-
import math as mathLib

class Vec3():
    """
        Vec3 definition
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):

        return "X : {0} ; Y : {1}; Z : {2} ;".format(self.x, self.y, self.z)

    def __add__(self, other):
        """
            Simple vec3 adition
        """
        out = Vec3()

        out.x = self.x + other.x
        out.y = self.y + other.y
        out.z = self.z + other.z

        return out

    def __sub__(self, other):
        """
            Simple vec3 substraction
        """
        out = Vec3()

        out.x = self.x - other.x
        out.y = self.y - other.y
        out.z = self.z - other.z

        return out

    def __mul__(self, other):
        """
            Simple Vec3 dot product
        """
        # To avoid type errors
        if not isinstance(other, Vec3):

            return self.__rmul__(other)

        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def __rmul__(self, other):
        """
            Simple Vec3 scalar product
        """
        out = Vec3()

        out.x = self.x * other
        out.y = self.y * other
        out.z = self.z * other

        return out

    def __pow__(self, inVec):
        """
            Simple Vec3 cross product
        """
        outVec = Vec3()

        out.x = self.y * inVec.z - self.z * inVec.y
        out.y = self.z * inVec.x - self.x * inVec.z
        out.z = self.x * inVec.y - self.y * inVec.x

        return out

    def __eq__(self, other):
        """

        """
        return self.x==other.x and self.y==other.y and self.z==other.z

    def normalize(self):
        """
            Normalizes the vector
        """
        length = self.length()

        if length > 0.0:
            self.x /= length
            self.y /= length
            self.z /= length

    def length(self):
        """
            Returns the length of the vector
        """
        return mathLib.sqrt(self * self)


class Point3():
    """
        Point3 definition
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):

        return "X : {0} ; Y : {1}; Z : {2} ;".format(self.x, self.y, self.z)

    def __sub__(self, other):
        """
            Returns the vector going from one point to the other
        """
        out = Vec3()

        out.x = self.x - other.x
        out.y = self.y - other.y
        out.z = self.z - other.z

        return out
