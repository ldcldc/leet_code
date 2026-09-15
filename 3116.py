import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        sorted_coins = sorted(coins)
        left = sorted_coins[0]
        right = sorted_coins[0] * k
        result = right
        
        combination_coins = []
        lcm_coins = []
            
        for i in range(len(sorted_coins)):
            combination_coins.append(list(combinations(sorted_coins, i+1)))
            lcm_coins.append([math.lcm(*combination) for combination in combination_coins[i]])

        while(left <= right):
            mid = (left + right)//2
            count = 0
            
            for lcms in lcm_coins[::2]:
                for lcm in lcms:
                    count += mid//lcm
            for lcms in lcm_coins[1::2]:
                for lcm in lcms:
                    count -= mid//lcm

            if left >= right:
                if count != k:
                    return mid + 1
                return mid
            if count < k:
                left = mid + 1
            else :
                right = mid - 1
                result = mid
        return result

    def findKthSmallest_2(self, coins: list[int], k: int) -> int:
        
        n = len(coins)
        left = 1
        right = min(coins) * k
        answer = right

        def lcm(a, b):
            return (a * b) // math.gcd(a, b)
        

        # 비트마스킹
        subsets = []
        for i in range(1, 1 << n):  # 1 ~ 2^n - 1까지
            curr_lcm = 1
            bits = 0
            for j in range(n):
                if i & (1 << j):
                    curr_lcm = lcm(curr_lcm, coins[j])
                    bits += 1
            """
            sign * (mid // curr_lcm)과 mid // (sign * curr_lcm)는 결과가 다르다
            ex) mid = 25, sign = -1, curr_lcm = 10 일때
                sign * (mid // curr_lcm) = -1 * (25//10) = -2 이고(2.5에서 내림)
                mid // (sign * curr_lcm) = 25 // -10 = -3 이다 (-2.5에서 내림)
                
                a//b 는 b가 0이외에도 음수일때도 조심
            """
            sign = 1 if bits % 2 != 0 else -1
            subsets.append((curr_lcm, sign))

        
        while left <= right:
            mid = (left + right) // 2

            count = 0
            for curr_lcm, sign in subsets:
                count += sign * (mid // curr_lcm)
                
            if count >= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return answer

        
a = Solution()
print(a.findKthSmallest([3,8,7],6))