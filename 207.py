from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        num_entry = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        length = 0
        queue = deque()

        for u, v in prerequisites:
            num_entry[u] += 1
            graph[v].append(u)

        # queue = deque([i for i in range(numCourses) if num_entry[i] == 0])
        for i in range(numCourses):
            if not num_entry[i]:
                queue.append(i)
            
        while queue:
            curr_course = queue.popleft()
            length += 1
            for i in graph[curr_course]:
                num_entry[i] -= 1
                if not num_entry[i]:
                    queue.append(i)
        
        return length == numCourses