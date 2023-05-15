# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #pointer one
        cur = head
        for i in range(k-1):
            cur = cur.next

        #storing the left pointer which need to be swap 
        left = cur
        right = head #storing the right pointer which need to be swap

        #iterating over the list to get the correct right pointer
        while cur.next:
            cur = cur.next
            right = right.next

        #swap left pointer & right pointer node value
        left.val,right.val = right.val,left.val

        return head