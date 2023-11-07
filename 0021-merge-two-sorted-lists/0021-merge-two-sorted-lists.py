# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        
        # EMPTY NODE
        merge_head = ListNode(3)
        temp = merge_head
        
        while head1 and head2:
            if head1.val <= head2.val:
                new_node = ListNode(head1.val)
                temp.next = new_node
                head1 = head1.next
                temp = temp.next
            else:
                new_node = ListNode(head2.val)
                temp.next = new_node
                head2 = head2.next
                temp = temp.next
        while head1:
            new_node = ListNode(head1.val)
            temp.next = new_node
            head1 = head1.next
            temp = temp.next
        while head2:
            new_node = ListNode(head2.val)
            temp.next = new_node
            head2 = head2.next
            temp = temp.next
        
        merge_head = merge_head.next
        return merge_head