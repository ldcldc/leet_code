class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
        while(num):
            length = 1
            curr_num = num.pop()
            num_temp = curr_num
            while(num_temp + 1 in num):
                num_temp += 1
                num.remove(num_temp)
                length += 1
            num_temp = curr_num
            while(num_temp - 1 in num):
                num_temp -= 1
                num.remove(num_temp)
                length += 1
            longest = max(length,longest)
        return longest
    
    def longestConsecutive_2(self, nums: list[int]) -> int:
        num = set(nums)
        longest = 0
        for n in num:
            if n-1 not in num:
                length = 1
                while(n + length in num):
                    length += 1
                longest = max(longest, length)
        return longest

nums = [100,4,200,1,3,2]
a = Solution()
print(a.longestConsecutive_2(nums))