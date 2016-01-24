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
        self.y = z

    def __str__(self):
        
        return {"X":self.x,"Y":self.y, "Z":self.z}


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
            Simple vec3 dot product
        """
        # To avoid type errors
        if not isinstance(other, Vec3):

            return self.__rmul__(other)

        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def __rmul__(self, other):
        """
            Simple vec3 scalar product
        """
        out = Vec3()

        out.x = self.x * other
        out.y = self.y * other
        out.z = self.z * other

        return out

    def normalize(self):
        """
            Normalizes the vector
        """
        length = mathLib.sqrt(self * self)

        if length > 0.0:
            self.x /= length
            self.y /= length
            self.z /= length

            return True

        return None
