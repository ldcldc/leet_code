from collections import defaultdict

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        
        cur_count = defaultdict(int)
        
        for num in nums:
            val = num % k
            next_count = defaultdict(int)
            
            next_count[val] += 1
            
            for r, count in cur_count.items():
                new_r = (r * val) % k
                next_count[new_r] += count
                
            for r, count in next_count.items():
                res[r] += count
                
            cur_count = next_count
            
        return res
    
a = Solution()
print(a.resultArray([1,2,3,4,5],3))