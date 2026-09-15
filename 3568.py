from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom[0])
        n = len(classroom)
        
        L_count = 0
        L_index = {}
        s_x = -1
        s_y = -1
        
        for x in range(m):
            for y in range(n):
                if classroom[y][x] == 'L':
                    L_index[(x,y)] = L_count
                    L_count += 1
                    
                if classroom[y][x] == 'S':
                    s_x, s_y = x, y
                    
        L_total = (1 << L_count) - 1
        best_energy = [[[-1 for _ in range(1 << L_count)] for _ in range(n)] for _ in range(m)]

        queue = deque([[s_x,s_y,0,energy,0]])
        
        while queue:
            x,y,bit_mask,e, num_moves = queue.popleft()
            
            if classroom[y][x] == 'X':
                continue
            
            if classroom[y][x] == 'R':
                e = energy
            
            if classroom[y][x] == 'L':
                bit_mask |= (1 << L_index[(x, y)])
                
            if best_energy[x][y][bit_mask] >= e:
                continue
            best_energy[x][y][bit_mask] = e
            
            if bit_mask == L_total:
                return num_moves

            if e == 0:
                continue

            if x != 0:
                queue.append([x-1,y,bit_mask,e-1, num_moves+1])
            if x != m-1:
                queue.append([x+1,y,bit_mask,e-1, num_moves+1])
            if y != 0:
                queue.append([x,y-1,bit_mask,e-1, num_moves+1])
            if y != n-1:
                queue.append([x,y+1,bit_mask,e-1, num_moves+1])
        return -1
    
a = Solution()
b = a.minMoves(["LR..R", "..SLX"],9)
print(b)