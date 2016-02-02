# _Accelerator_V_001.py
from .PR_CONSTANTS import INF, PRIMLIMIT, DEPTHLIMIT

class RT_Accelerator():
    def __init__(self, primList, bounds, depth=0, avoid_checking=False):
        """
            Node owner must pass a primitive list and bounds.
            For every primitive it calls the primitive method intersect_aabb
            with self.bounds as parameter, if primitive intersects we add.

            el node padre debe pasarle:     -Los limites(los del nodo hijo).
                                            -La lista de primitivas(del padre).
            Genera una lista auxiliar de bool del mismo tamaño que la de primitivas.
            Recorre las primitivas para determinar si hay interseccion con el nodo, y
             marca el resultado en la lista auxiliar.
            A partir de ambas listas genera la lista de primitivas propia.
            Si no esta vacia entonces:
                -Recalcula los limites para intentar reducirlos.
                -Determina si necesita dividirse:
                    -Determina los limites estimados de los nodos hijo.
                    -Genera los nodos hijo.
                    -Si el nodo hijo esta vacio, lo elimina.
        """
        # We set this limits for initializing, later we'll adjust them
        self.bounds = bounds
        # Primitive iterator
        self.primitives = []
        # If avoid_checking set to True we accept the primitive without checking
        if not avoid_checking:
            for primitive in primList:
                if primitive.intersects_aabb(self.bounds):
                    self.primitives.append(primitive)
        else:
            self.primitives = primList
        # Adjusting the limits. If self.primitives is empty does nothing.
        self.set_limits()
        # Child nodes iterator
        self.childs = []
        #
        if len(self.primitives) > PRIMLIMIT and depth < DEPTHLIMIT:
            self.initialize_childs()
        # It's done!!

    def initialize_childs(self):
        limitX = self.limits["maxX"] + self.limits["minX"] * 0.5
        limitY = self.limits["maxY"] + self.limits["minY"] * 0.5
        limitZ = self.limits["maxZ"] + self.limits["minZ"] * 0.5
        # U_U_U
        childBounds = { "maxX":limitX,"minX":self.limits["minX"],
                        "maxY":limitY,"minY":self.limits["minY"],
                        "maxZ":limitZ,"minZ":self.limits["minZ"]}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # U_U_D
        childBounds = { "maxX":limitX,"minX":self.limits["minX"],
                        "maxY":limitY,"minY":self.limits["minY"],
                        "maxZ":self.limits["maxZ"],"minZ":limitZ}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # U_D_U
        childBounds = { "maxX":limitX,"minX":self.limits["minX"],
                        "maxY":self.limits["maxY"],"minY":limitY,
                        "maxZ":limitZ,"minZ":self.limits["minZ"]}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # U_D_D
        childBounds = { "maxX":limitX,"minX":self.limits["minX"],
                        "maxY":self.limits["maxY"],"minY":limitY,
                        "maxZ":self.limits["maxZ"],"minZ":limitZ}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # D_U_U
        childBounds = { "maxX":self.limits["maxX"],"minX":limitX,
                        "maxY":limitY,"minY":self.limits["minY"],
                        "maxZ":limitZ,"minZ":self.limits["minZ"]}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # D_U_D
        childBounds = { "maxX":self.limits["maxX"],"minX":limitX,
                        "maxY":limitY,"minY":self.limits["minY"],
                        "maxZ":self.limits["maxZ"],"minZ":limitZ}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # D_D_U
        childBounds = { "maxX":self.limits["maxX"],"minX":limitX,
                        "maxY":self.limits["maxY"],"minY":limitY,
                        "maxZ":limitZ,"minZ":self.limits["minZ"]}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)
        # D_D_D
        childBounds = { "maxX":self.limits["maxX"],"minX":limitX,
                        "maxY":self.limits["maxY"],"minY":limitY,
                        "maxZ":self.limits["maxZ"],"minZ":limitZ}

        child = RT_Accelerator(self.primitives,childBounds,depth=depth+1)
        if len(child.primitives) > 0:
            self.childs.append(child)


    def __str__(self):
        sChildDepth = "Child depth : {} levels\n".format(self.child_depth)
        triangleCount = 0
        if self.content:

            triangleCount = len(self.content)

        sContent = "Triangle count : {} triangles\n".format(triangleCount)

        sLimits = self.bounds.__str__()

        return sChildDepth + sContent + sLimits

    def set_limits(self):
        if len(self.primitives) > 0:

            self.limits["minX"] = min(map((lambda x: min(x.p1.x,x.p2.x,x.p3.x)),self.triangles))
            self.limits["maxX"] = max(map((lambda x: max(x.p1.x,x.p2.x,x.p3.x)),self.triangles))
            self.limits["minY"] = min(map((lambda x: min(x.p1.y,x.p2.y,x.p3.y)),self.triangles))
            self.limits["maxY"] = max(map((lambda x: max(x.p1.y,x.p2.y,x.p3.y)),self.triangles))
            self.limits["minZ"] = min(map((lambda x: min(x.p1.z,x.p2.z,x.p3.z)),self.triangles))
            self.limits["maxZ"] = max(map((lambda x: max(x.p1.z,x.p2.z,x.p3.z)),self.triangles))
