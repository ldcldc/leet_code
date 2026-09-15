from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        
        for i in range(1,len(nums)):
            dp[i] = max((dp[j] + 1 for j in range(i) if nums[j] < nums[i]), default=1)
        return max(dp)

    def lengthOfLIS_2(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            idx = bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)
                    
a = Solution()
print(a.lengthOfLIS([1,3,6,7,9,4,10,5,6]))