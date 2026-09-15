class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            count = 1   
            curr_sum = 0   
            
            for num in nums:
                if curr_sum + num > mid:
                    count += 1     
                    curr_sum = num  
                else:
                    curr_sum += num 

            if count <= k:
                result = mid 
                right = mid - 1   
            else:
                left = mid + 1
                
        return result
    
a = Solution()
print(a.splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8],8))