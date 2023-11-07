# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                nextN = curr.next
                curr.next = prev
                prev = curr
                curr = nextN
                
            return prev
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        if fast is None:
            head1 = reverse(slow)
        else:
            head1 = reverse(slow.next)
        # temp = head
        # temp1 = head1.next
        
        while head and head1:
            if head.val != head1.val:
                return False
            head = head.next
            head1 = head1.next
        
        print(head)
        print(head1)
        return True
            
            