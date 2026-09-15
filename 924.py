from collections import Counter

class network:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_nodes = [1] * n
        
    def union(self, index1, index2):
        index1 = self.find_parent(index1)
        index2 = self.find_parent(index2)
        if index1 == index2:
            return
        
        if self.num_nodes[index1] < self.num_nodes[index2]:
            index1, index2 = index2, index1
        self.num_nodes[index1] += self.num_nodes[index2]
        self.parent[index2] = self.parent[index1]
        
    def find_parent(self, index):
        if self.parent[index] == index:
            return index
        self.parent[index] = self.find_parent(self.parent[index])
        return self.parent[index]

class Solution:
    def minMalwareSpread_2(self, graph: List[List[int]], initial: List[int]) -> int:
        net = network(len(graph))
        
        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                if graph[i][j] == 1:
                    net.union(i, j)

        parent_count = Counter([net.find_parent(node) for node in initial])
        
        min_index = -1
        max_size = 0
        
        for index in initial:
            parent = net.find_parent(index)
            if parent_count[parent] == 1:
                size = net.num_nodes[parent]
                
                if size > max_size or (size == max_size and index < min_index):
                    min_index = index
                    max_size = size
        
        return min(initial) if min_index == -1 else min_index

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        
        def dfs(i):
            is_visited[i] = True
            visited.add(i)
            
            for j in range(len(graph)):
                if graph[i][j] == 1 and not is_visited[j]:
                    dfs(j)

        networks = []
        is_visited = [False] * len(graph)
        
                
        for i in range(len(graph)):
            if not is_visited[i]:
                visited = set()
                dfs(i)
                networks.append([visited,len(visited)])
        
        num_malware = [[] for i in range(len(networks))]
        for init in initial:
            for i in range(len(networks)):
                if init in networks[i][0]:
                    num_malware[i].append(init)
                    
        min_m_index = (-1,-1)
        for i in range(len(num_malware)):
            if len(num_malware[i]) == 1:
                if min_m_index[0] == -1 or networks[i][1] > networks[min_m_index[1]][1] or (networks[i][1] == networks[min_m_index[1]][1] and num_malware[i][0] < min_m_index[0]):
                    min_m_index = (num_malware[i][0], i)

        return min(initial) if min_m_index[0] == -1 else min_m_index[0]
    
    
a = Solution()
print(a.minMalwareSpread_2([[1,1,1],[1,1,1],[1,1,1]], [1,2]))