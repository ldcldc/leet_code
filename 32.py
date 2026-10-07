class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_length = 0
        start = len(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                start = min(start, i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_length = max(max_length, i - stack[-1])
                    else:
                        max_length = max(max_length, i - start + 1)
                else:
                    start = len(s)
        return max_length

    def longestValidParentheses_2(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length

    def longestValidParentheses_3(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        max_length = 0
        
        for i in range(1, n):
            if s[i] == ')':
                # ()
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                    
                # ( (...) )
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0)
                    
                max_length = max(max_length, dp[i])
                
        return max_length

    def longestValidParentheses_4(self, s: str) -> int:
        left = right = max_length = 0
        
        for c in s:
            if c == '(': left += 1
            else: right += 1
            
            if left == right:
                max_length = max(max_length, right)
            elif right > left:
                left = right = 0
                
        left = right = 0
        
        for c in reversed(s):
            if c == '(': left += 1
            else: right += 1
            
            if left == right:
                max_length = max(max_length, left)
            elif left > right:
                left = right = 0
                
        return max_length * 2
                
            
a = Solution()
print(a.longestValidParentheses("()(()"))