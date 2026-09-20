import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        
        c_p = sorted([(capital[i], profits[i]) for i in range(n)])
        
        pq = []
        in_heap = set()
        
        index = 0
        
        for _ in range(k):
            if len(in_heap) != n:
                for i in range(index, n):
                    if c_p[i][0] <= w:
                        heapq.heappush(pq, -c_p[i][1])
                        in_heap.add(i)
                        index = i + 1
                    else:
                        break
            if not len(pq):
                break
            w += -heapq.heappop(pq)
        return w

a = Solution()
print(a.findMaximizedCapital(10, 0, [1,2,3], [0,1,2]))