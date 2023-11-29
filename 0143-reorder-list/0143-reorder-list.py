# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        middle = self.find_middle(head)
        
        # reverse second_half
        second_half = self.reverse_list(middle.next)
        middle.next = None
        
        self.merge_lists(head, second_half)
        
    def find_middle(self,head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    
    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
    
    def merge_lists(self, l1: ListNode, l2: ListNode) -> None:
        while l1 and l2:
            next_l1 = l1.next
            next_l2 = l2.next
            
            l1.next = l2
            l2.next = next_l1
            
            l1 = next_l1
            l2 = next_l2    