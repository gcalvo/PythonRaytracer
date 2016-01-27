# _Accelerator_V_001.py
from .PR_CONSTANTS import INF

class RT_Accelerator():
    def __init__(self, depth=0):
        self.bounds = { "maxX":-INF,
                        "maxY":-INF,
                        "maxZ":-INF,
                        "minX":INF,
                        "minY":INF,
                        "minZ":INF }
        # Child accelerators
        self.childs = None
        # triangle list
        self.content = None

        if depth > 1 :

            self.initialize_childs(depth=(depth - 1))

        self.childs_depth = depth - 1

    def __str__(self):
        sChildDepth = "Child depth : {} levels\".format(self.child_depth)
        triangleCount = 0
        if self.content:

            triangleCount = len(self.content)

        sContent = "Triangle count : {} triangles\n".format(triangleCount)

        sLimits = self.bounds.__str__()

        return sChildDepth + sContent + sLimits

    def initialize_childs(self, depth=0):
        if not self.childs:
            if depth > 0:

                self.childs =   {   "U_U_U":RT_Accelerator(depth=depth),
                                    "U_U_D":RT_Accelerator(depth=depth),
                                    "U_D_U":RT_Accelerator(depth=depth),
                                    "U_D_D":RT_Accelerator(depth=depth),
                                    "D_U_U":RT_Accelerator(depth=depth),
                                    "D_U_D":RT_Accelerator(depth=depth),
                                    "D_D_U":RT_Accelerator(depth=depth),
                                    "D_D_D":RT_Accelerator(depth=depth)    }
        else:
            print("This RT_Accelerator is already initialized, use subdivide instead.")


    def insert_triangle(self, tri):
        """
            Insert input triangle to self.content or self.childs
        """
        if not self.childs:
            if not self.content:

                self.content = []

            self.content.insert(tri)
        else:
            self.insert_in_childs(tri)

    def insert_in_childs(self, tri):

        limitX = self.maxX + self.minX) * 0.5
        limitY = self.maxY + self.minY) * 0.5
        limitZ = self.maxZ + self.minZ) * 0.5

        maxX = max(tri.p1.x,tri.p3.x,tri.p3.x)
        minX = min(tri.p1.x,tri.p3.x,tri.p3.x)
        maxY = max(tri.p1.y,tri.p3.y,tri.p3.y)
        minY = min(tri.p1.y,tri.p3.y,tri.p3.y)
        maxZ = max(tri.p1.z,tri.p3.z,tri.p3.z)
        minZ = min(tri.p1.z,tri.p3.z,tri.p3.z)

        if maxX < limitX:
            if maxY < limitY:
                if maxZ < limitZ:
                    self.childs["D_D_D"].insert_triangle(tri)
                elif minZ > limitZ:
                    self.childs["D_D_U"].insert_triangle(tri)
                else:
                    self.split_triangle(tri)
            elif minY > limitY:
                if maxZ < limitZ:
                    self.childs["D_U_D"].insert_triangle(tri)
                elif minZ > limitZ:
                    self.childs["D_U_U"].insert_triangle(tri)
                else:
                    self.split_triangle(tri)
        elif minX > limitX:
            if maxY < limitY:
                if maxZ < limitZ:
                    self.childs["U_D_D"].insert_triangle(tri)
                elif minZ > limitZ:
                    self.childs["U_D_U"].insert_triangle(tri)
                else:
                    self.split_triangle(tri)
            elif minY > limitY:
                if maxZ < limitZ:
                    self.childs["U_U_D"].insert_triangle(tri)
                elif minZ > limitZ:
                    self.childs["U_U_U"].insert_triangle(tri)
                else:
                    self.split_triangle(tri)
        else:
            self.split_triangle(tri)

    def purge_empty_childs(self):
        """
            Deletes recursively empty accelerating structures
        """
        if self.childs:

            for childName, child in self.childs.items():

                if not child.childs:
                    if not child.content:

                        delete(child)
                        self.childs[childName] = None
                else:

                    child.purge_empty_childs()

    def subdivide(self):
        if not self.childs:

            self.initialize_childs()

            if self.content :

                for tri in self.content:
                    self.insert_in_childs(tri)

                delete(self.content)
                self.content = None

        else:

            for childName, child in self.childs.items():
                child.subdivide()

    def split_triangle(self, tri):
        limitX = self.maxX + self.minX) * 0.5
        limitY = self.maxY + self.minY) * 0.5
        limitZ = self.maxZ + self.minZ) * 0.5

        if tri.p1.x > limitX:
            if tri.p2.x > limitX:
                if tri.p3.x < limitX: #p3 is in the opposite side of limitX
                    print("P3 en el eje X")
            else:
                if tri.p3.x > limitX:
                    print("P2 en el eje X")
                else:
                    print("P2 y P3 en el eje X")
        else:
            if tri.p2.x < limitX:
                if tri.p3.x > limitX: #p3 is in the opposite side of limitX
                    print("P1 y P2 en el eje X")
            else:
                if tri.p3.x > limitX:
                    print("P2 en el eje X")
                else:
                    print("P1 en el eje X")





        maxX = max(tri.p1.x,tri.p3.x,tri.p3.x)
        minX = min(tri.p1.x,tri.p3.x,tri.p3.x)
        maxY = max(tri.p1.y,tri.p3.y,tri.p3.y)
        minY = min(tri.p1.y,tri.p3.y,tri.p3.y)
        maxZ = max(tri.p1.z,tri.p3.z,tri.p3.z)
        minZ = min(tri.p1.z,tri.p3.z,tri.p3.z)
