# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=slow=head
        
        while fast and fast.next:
            fast = fast.next.next
            slow =slow.next

        halfHead = None
        nxt = slow.next
        slow.next = None
        slow = nxt
        while slow:
            nxt = slow.next
            slow.next = halfHead
            halfHead = slow
            slow=nxt

        l1 = head
        l2 = halfHead


        while l2:

            l1snxt  = l1.next
            l2snxt  = l2.next

            l1.next = l2
            l2.next = l1snxt

            l1 = l1snxt
            l2 = l2snxt