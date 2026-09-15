# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        node_dp = {}
        
        def postorder(node):
            if node.left is None:
                left_max = 0
            else:
                postorder(node.left)
                left_max = node_dp[node.left.val][1]
            if node.right is None:
                right_max = 0
            else:
                postorder(node.right)
                right_max = node_dp[node.right.val][1] 
                
            # corner = 이 노드가 경로의 꼭짓점일때(이 경로속 노드중 최상단일 때)의 max
            # via = 이 경로속 노드중 최상단이 아닐 때의 max
            corner = node.val + max(left_max,0) + max(right_max,0)
            via = node.val + max(left_max,right_max,0)
            node_dp[node.val] = (corner, via)
            
        postorder(root)
        
        return max(max(corner, via) for corner, via in node_dp.values())
    
    
    
    def maxPathSum_2(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_max = max(dfs(node.left),0)
            right_max = max(dfs(node.right),0)
            
            corner_max = left_max + right_max + node.val
            max_sum = max(max_sum, corner_max)
            
            return node.val + max(left_max,right_max,0)
            
        dfs(root)
        return max_sum