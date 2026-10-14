class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        num_bit = [0]*31
        res = 0
        for num in nums:
            for i in range(31):
                num_bit[i] += 1 if num & 1 else 0
                num >>= 1
                if not num:
                    break
        
        first_one = 29
        
        is_first = 0
        for i in range(k):
            if is_first:
                break
            is_first = 1
            num = 0
            for j in range(first_one, -1, -1):
                if num_bit[j]:
                    if is_first:
                        first_one = j
                        is_first = 0
                    num += 1 << j
                    num_bit[j] -= 1
            res = (res + num*num) % (10**9 + 7)
        return res
            
a = Solution()
print(a.maxSum(nums = [14,45,76,33,35,53,67,19,6,31,33], k = 10))