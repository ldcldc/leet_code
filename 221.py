class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(val) for val in row] for row in matrix]
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for i in range(n+1)]
        max_squ = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                print(f'i = {i}, j = {j}')
                x, y = i, j
                while(x<m+1 and y<n+1):
                    isone = True
                    if dp[j][i-1]-1 < x-i+1 and dp[j-1][i]-1 < x-i+1:
                        for k in range(x-i+1):
                            if not matrix[y-1][x-k-1] or not matrix[y-k-1][x-1]:
                                isone = False
                                break
                    if isone:
                        dp[j][i] += 1 
                        max_squ = max(max_squ, dp[j][i])
                    else:
                        break
                    x += 1
                    y += 1
        return max_squ*max_squ
    
    
    def maximalSquare_2(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_squ = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_squ = max(max_squ, dp[i][j])
                    
        return max_squ * max_squ
    
a = Solution()
print(a.maximalSquare_2([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]))