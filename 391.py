class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:      
        area = 0
        vertices = set()
        
        for vertex in rectangles:
            if (vertex[0],vertex[1]) in vertices:
                vertices.remove((vertex[0],vertex[1]))
            else:
                vertices.add((vertex[0],vertex[1]))
            if (vertex[0],vertex[3]) in vertices:
                vertices.remove((vertex[0],vertex[3]))
            else:
                vertices.add((vertex[0],vertex[3]))
            if (vertex[2],vertex[1]) in vertices:
                vertices.remove((vertex[2],vertex[1]))
            else:
                vertices.add((vertex[2],vertex[1]))
            if (vertex[2],vertex[3]) in vertices:
                vertices.remove((vertex[2],vertex[3]))
            else:
                vertices.add((vertex[2],vertex[3]))
            area += (vertex[2] - vertex[0]) * (vertex[3] - vertex[1])
            
        vertices = list(vertices)
        
        print(vertices,area)
        
        if len(vertices) == 4:
            if vertices[0][0] == vertices[1][0]:
                y = abs(vertices[0][0] - vertices[2][0])
                x = abs(vertices[0][1] - vertices[1][1])
            else:
                y = abs(vertices[0][0] - vertices[1][0])
                if vertices[0][1] == vertices[1][1]:
                    x = abs(vertices[0][1] - vertices[2][1])
                else:
                    x = abs(vertices[0][1] - vertices[1][1])
            print(x,y)
            if area != x*y:
                return False
            return True
        return False

    
a = Solution()
print(a.isRectangleCover([[0,0,4,1]]))