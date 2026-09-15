class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def reculsion(grid):
            n = len(grid)
            temp = grid[0][0]
            leaf = True
            
            for i in range(n):
                if not leaf:
                    break
                for j in range(n):
                    if not leaf:
                        break
                    if grid[i][j] != temp:
                        leaf = False
                        
                        topLeftNode = reculsion([row[:n//2] for row in grid[:n//2]])
                        topRightNode = reculsion([row[n//2:] for row in grid[:n//2]])
                        bottomLeftNode = reculsion([row[:n//2] for row in grid[n//2:]])
                        bottomRightNode = reculsion([row[n//2:] for row in grid[n//2:]])
                        
            
            #node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
            if leaf:
                return Node(temp,1,None,None,None,None)           
            else:
                return Node(1,0,topLeftNode,topRightNode,
                                bottomLeftNode,bottomRightNode)
                
        def reculsion_2(x,y,size):          # 해당 노드는(x,y)에서 시작하고 크기는 size
            size_next = size//2
            temp = grid[y][x]
            
            for i in range(y, y + size):
                for j in range(x, x + size):
                    if grid[i][j] != temp:
                        return Node(1,
                                    0,
                                    reculsion_2(x,y,size_next),
                                    reculsion_2(x+size_next,y,size_next),
                                    reculsion_2(x,y+size_next,size_next),
                                    reculsion_2(x+size_next,y+size_next,size_next))

            return Node(temp,1,None,None,None,None)           
                    
        #return reculsion(grid)
        return reculsion_2(0,0,len(grid))
