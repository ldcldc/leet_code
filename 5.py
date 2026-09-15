class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        start, max_len = 0, 0
        
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len_odd = expand(i, i)
            len_even = expand(i, i + 1)
            
            current_max = max(len_odd, len_even)
            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2
                
        return s[start:start + max_len]
    
    def longestPalindrome_2(self, s: str) -> str:
        n = len(s)
        
        dp = [[0]*i for i in range(n,0,-1)]
        
        for j in range(n):
            for i in range(n-j):
                if i == j+i:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j+i]:
                        if i+1 <= j+i-1:
                            if dp[i+1][j-2]:
                                dp[i][j] = dp[i+1][j-2] + 2
                        else:
                            dp[i][j] = 2
        max_row, max_len = max(((r, val) for r, row in enumerate(dp) for val in row),key=lambda x: x[1])
        return s[max_row:max_row+max_len]
    
    def longestPalindrome_3(self, s: str) -> str:
        n = len(s)
        
        dp = [[False]*i for i in range(n,0,-1)]
        
        max_len = (1, 0)
        
        for j in range(n):      #j = 길이
            for i in range(n-j):#i = 시작점
                if j == 0 or (s[i] == s[i+j] and (j == 1 or dp[i+1][j-2])):
                    dp[i][j] = True
                    max_len = max(max_len, (j+1, i))
                    
        (max_j, max_i) = max_len
        return s[max_i:max_i+max_j]
    
a = Solution()
print(a.longestPalindrome_3("hbddbh"))