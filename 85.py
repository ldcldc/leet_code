class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        one_nums = [[(0,0)] * (m + 1) for _ in range(n + 1)]
        max_rec = 0
         
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i-1][j-1] == '1':
                    one_nums[i][j] = (one_nums[i-1][j][0] +1,one_nums[i][j-1][1] +1)
                    
                    one_up = one_nums[i][j][0]
                    area = []
                    for k in range(1,one_nums[i][j][1]+1):
                        if one_up > one_nums[i][j - k][0]:
                            area.append(k * one_up)
                            one_up = one_nums[i][j - k][0]
                    
                    max_rec = max(max_rec, max(area))

        return max_rec
    
    def maximalRectangle_2(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        
        one_nums = [[0] * (m + 1) for _ in range(n + 1)]
        max_rec = 0
        
        
        for i in range(1, n + 1):
            stack = [[0,0]]
            for j in range(1, m + 1):

                if matrix[i-1][j-1] == '1':
                    one_nums[i][j] = one_nums[i-1][j] +1

                if stack[-1][0] > one_nums[i][j]:
                    temp = []
                    while stack[-1][0] > one_nums[i][j]:
                        curr = stack.pop()
                        max_rec = max(max_rec, curr[0] * (j - curr[1]))
                        temp.append([one_nums[i][j],curr[1]])
                    stack.extend(temp)
                        
                if one_nums[i][j]:
                    stack.append([one_nums[i][j],j])
                    
                if j == m:
                    while stack[-1][0] > 0:
                        curr = stack.pop()
                        max_rec = max(max_rec, curr[0] * (j - curr[1] + 1))
        
        return max_rec
    
    def maximalRectangle_3(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
            
        n = len(matrix)
        m = len(matrix[0])

        heights = [0] * (m + 1) 
        max_rec = 0
        
        for i in range(n):
            stack = []
            for j in range(m + 1):
                if j < m:
                    if matrix[i][j] == '1':
                        heights[j] += 1
                    else:
                        heights[j] = 0
                
                curr_h = heights[j]
                start = j
                
                while stack and stack[-1][0] > curr_h:
                    prev_h, prev = stack.pop()
                    max_rec = max(max_rec, prev_h * (j - prev))
                    start = prev
                
                stack.append([curr_h, start])
                
        return max_rec
    
a = Solution()
print(a.maximalRectangle_2(matrix = [["1","0","0","0","1"],["1","1","0","1","1"],["1","1","1","1","1"]]))