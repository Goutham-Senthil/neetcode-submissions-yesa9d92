# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nHead = None
        curr = head
        while curr:
            #store the next variable
            nxt = curr.next 

            #point the current to the new head
            curr.next = nHead

            #the current variable is now the new head
            nHead = curr

            curr = nxt
        
        return nHead