class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jumps = {stone:set() for stone in stones}
        if 1 in jumps:
            jumps[1].add(1) 
        else:
            return False
        
        if len(stones) == 2:
            return True
                
        for stone in jumps:
            if jumps[stone]:
                for jump in jumps[stone]:
                    for k in range(3):
                        if stone + jump - 1 + k in jumps and not stone + jump - 1 + k == stone:
                            if stone + jump - 1 + k == stones[-1]:
                                return True
                            jumps[stone + jump - 1 + k].add(jump - 1 + k)
        
        return False


a = Solution()
print(a.canCross([0,1,3,5,6,8,12,17]))