#!/usr/bin/python
# -*- encoding: utf-8 -*-

class RGBAColor():
    """
        RGBAColor definition
        Values are restricted to [0.0,1.0]
    """
    def __init__(self, red = 0.0, green=0.0, blue=0.0, alpha=1.0):
        self.R = max(0.0, min(1.0, red))
        self.G = max(0.0, min(1.0, green))
        self.B = max(0.0, min(1.0, blue))
        self.A = max(0.0, min(1.0, alpha))

    def __str__(self):
        return {"R":self.red,"G":self.G, "B":self.B, "A":self.A}

    def __setattr__(self, nomAttr, valAttr):
        """
            Set Attribute override for check value limits
        """
        realVal = max(0.0, min(1.0, valAttr))
        object.__setattr__(nomAttr, realVal)

    def __add__(self, other):
        """
            Simple color adition, not alpha-weighted
        """
        outColor = RGBAColor()
        outColor.R = min(1.0, self.R + other.R)
        outColor.G = min(1.0, self.G + other.G)
        outColor.B = min(1.0, self.B + other.B)
        outColor.A = min(1.0, self.A + other.A)

        return outColor

    def __sub__(self, other):
        """
            Simple color substraction, not alpha-weighted
        """
        outColor = RGBAColor()
        outColor.R = max(0.0, self.R - other.R)
        outColor.G = max(0.0, self.G - other.G)
        outColor.B = max(0.0, self.B - other.B)
        outColor.A = max(0.0, self.A - other.A)

        return outColor
