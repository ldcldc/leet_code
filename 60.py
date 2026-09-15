import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        goal = k
        result = []
        
        for i in range(n-1,-1,-1):
            fact = math.factorial(i)
            temp = (goal-1)//fact
            goal -= fact*temp
            result.append(nums.pop(temp))
        
        output = ''
        
        for i in range(n):
            output = output + str(result.pop(0))
        return output
    
a= Solution()
print(a.getPermutation(4,9))
