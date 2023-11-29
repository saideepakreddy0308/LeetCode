# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            _sum = x + y + carry
            carry = _sum // 10
            
            current.next = ListNode(_sum % 10)
            
            # move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            # move to next result node
            current = current.next
        
        return dummy.next
    # T.C:  O(n), n be length of longer list
    # S.C: O(n), spaced used is proportional to length og longer llist. dummy -> new_node_x -> new_node_y 