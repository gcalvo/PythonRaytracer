# Camera definitions
from math import sin, cos
from ._Algebra_V_001 import Point3 as Point, Vec3 as Vector
from ._Geometry_V_001 import RayA as Ray
from .PR_CONSTANTS import DEGTORAD

class Camera():
    def __init__(self, from_point, to_vector, up_vector, aov, pixel_width, pixel_height):
        self.fromP = from_point
        self.toV = to_vector.normalize()
        self.upV = up_vector.normalize()
        self.AOV = aov # Refers to horizontal angle of view in degrees
        self.widthP = pixel_width
        self.heightP = pixel_height
        self.aspectRatio = self.widthP/self.heightP
        self._angle_step = self.AOV/self.widthP
        self._left_ref = self.upV**self.toV
        self.frameBuffer = range(self.withP * self.heightP)

    def getRay(self, pX, pY):
        angle_to = -0.5 * self.AOV + (float(pX) + 0.5) * self._angle_step)
        angle_to *= DEGTORAD
        angle_up = -0.5 * self.AOV/self.aspectRatio + (float(py) + 0.5) * self._angle_step
        angle_up *= DEGTORAD

        proy_to = cos(angle_to) * self.toV
        proy_left = sin(angle_to) * self._left_ref
        proy_up = sin(angle_up) * self.upV
        outDir = proy_to + proy_left + proy_up
        return Ray(self.fromP, outDir)

    def render(self, scene):
        for ix in range(self.widthP):
            for iy in range(self.heightP):
                index = ix + iy * self.widthP
                hitPointList = scene.Trace()
