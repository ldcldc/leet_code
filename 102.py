from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def preorder(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
  
            preorder(node.left,level + 1)
            preorder(node.right,level + 1)
                
        preorder(root, 0)
        
        return result

    def levelOrder_2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            same_level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                same_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(same_level)
            
        return result