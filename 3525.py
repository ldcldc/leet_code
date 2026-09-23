class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = [[0]*(k+1) for _ in range(len(nums) * 4)]

        def add(l_n, r_n):
            temp = l_n[:]
            for i in range(k):
                cur_i = (l_n[k] * i) % k
                temp[cur_i] += r_n[i]
        
            temp[k] = (l_n[k] * r_n[k]) % k  
            
            return temp
        
        def init(start, end, index):
            if start == end:
                val = nums[start] % k
                seg_tree[index][val] = 1
                seg_tree[index][k] = val
                return seg_tree[index]
                
            mid = (start + end) // 2
            
            seg_tree[index] = add(init(start, mid, index * 2),init(mid + 1, end, index * 2 + 1))
            
            return seg_tree[index]
                    
        def update(st, e, index, target, val):
            if st == e:
                nums[st] = val
                new_val = val % k

                seg_tree[index] = [0] * (k + 1) 
                seg_tree[index][new_val] = 1
                seg_tree[index][k] = new_val
                return
                
            mid = (st + e) // 2
            
            if target <= mid:
                update(st, mid, index * 2, target, val)
            else:
                update(mid + 1, e, index * 2 + 1, target, val)

            
            seg_tree[index] = add(seg_tree[index * 2],seg_tree[index * 2 + 1])
           

        def interval_mod(st, e, index, left, right):
            if left > e or right < st:
                return [0]*k + [1]
            if left <= st and right >= e:
                return seg_tree[index]
            
            mid = (st + e) // 2
            
            return add(interval_mod(st, mid, index * 2, left, right), interval_mod(mid + 1, e, index * 2 + 1, left, right))
        
        init(0, n - 1, 1)
        
        answer = []
        for idx, val, start_i, x_i in queries:
            update(0, n - 1, 1, idx, val)
            
            result_node = interval_mod(0, n - 1, 1, start_i, n - 1)
            
            answer.append(result_node[x_i])
            
        return answer


a = Solution()
print(a.resultArray(nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]))