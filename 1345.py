from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        conn = defaultdict(list)
        graph = [[] for _ in range(n)]
        graph[0].append(1)
        conn[arr[0]].append(0)
        graph[n-1].append(n-2)
        conn[arr[n-1]].append(n-1)
        
        for i in range(1, n-1):
            conn[arr[i]].append(i)
            graph[i].extend([i+1,i-1])
        
        print(conn)
        for i in range(n):
            print(graph[i])
        queue = deque()
        queue.append(0)
        count = 0
        is_visit = [0] * n
        is_visit[0] = 1
        
        while True:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == n-1: return count
                for i in conn[arr[curr]]:
                    if is_visit[i] == 0:
                        queue.append(i)
                        is_visit[i] = 1
                del conn[arr[curr]]
                for i in graph[curr]:
                    if is_visit[i] == 0:
                        queue.append(i)
                        is_visit[i] = 1
            count += 1

from collections import defaultdict, deque

class Solution:
    def minJumps_2(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        conn = defaultdict(list)
        for i, val in enumerate(arr):
            conn[val].append(i)
            
        queue = deque([0])
        is_visit = [0] * n
        is_visit[0] = 1
        count = 0
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                if curr == n - 1:
                    return count
                    
                for next in conn[arr[curr]]:
                    if is_visit[next] == 0:
                        is_visit[next] = 1
                        queue.append(next)
                del conn[arr[curr]]
                
                for next in (curr - 1, curr + 1):
                    if 0 <= next < n and is_visit[next] == 0:
                        is_visit[next] = 1
                        queue.append(next)
                        
            count += 1
            
        return count
a = Solution()
print(a.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]))