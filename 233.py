class Solution:
    def countDigitOne(self, n: int) -> int:
        #dp[i] = dp[i-1]*10 + 10^(i-1)
        print(f'in countDigitOne: n={n}')
        dp = [0, 1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000]
        
        if n < 10:
            print(f'base case: n={n}')
            return 1 if n >= 1 else 0
        
        l = len(str(n))
        for i in range(l, 0, -1):
            if n // (10**(i-1)) == 1:
                return dp[i-1] + (n % (10**(i-1))) + 1 + self.countDigitOne(n % (10**(i-1)))
            elif n // (10**(i-1)) > 1:
                return dp[i-1] * (n // (10**(i-1))) + (10**(i-1)) + self.countDigitOne(n % (10**(i-1)))
            
a = Solution()
print(a.countDigitOne(13))
            