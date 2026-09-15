class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr_node = head
        
        len_critical_points = []
        curr_status = 0
        pre_status = 0
        
        i = 0
        temp = 0        
        
        while(curr_node.next != None):
            
            next_node = curr_node.next
            
            if curr_node.val > next_node.val:
                curr_status = -1
            elif curr_node.val < next_node.val:
                curr_status = 1
            else:
                curr_status = 0
                
            if curr_status * pre_status == -1:
                if (i - temp) >= 0:
                    len_critical_points.append(i - temp)

                temp = i
            
            pre_status = curr_status
            curr_node = next_node
            i += 1
        
        if len(len_critical_points) < 2:
            return [-1,-1]
        
        if len_critical_points:
            del len_critical_points[0]
        
        return [min(len_critical_points), sum(len_critical_points)]