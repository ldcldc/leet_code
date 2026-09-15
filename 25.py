class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_node = ListNode(0,head)
        curr_node = head
        prev_node = head_node
        while(True):
            nodes = []
            for i in range(k):
                nodes.append(curr_node)
                if curr_node.next is None and i != k-1:
                    prev_node.next = nodes[0]
                    return head_node.next
                curr_node = curr_node.next
                
            for i in range(1,k):
                nodes[i].next = nodes[i-1]
            
            prev_node.next = nodes[k-1]
            prev_node = nodes[0]
            if curr_node is None:
                prev_node.next = None
                return head_node.next

class Solution:
    def reverseKGroup_2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            
            curr_node = group_prev.next
            group_prev.next = kth
            prev_node = kth.next
            group_prev = curr_node
            
            for _ in range(k):
                curr_node.next, prev_node, curr_node = \
                    prev_node, curr_node, curr_node.next
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr