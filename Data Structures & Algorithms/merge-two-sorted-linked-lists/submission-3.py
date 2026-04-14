# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        l1 = list1
        l2 = list2
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 101
            val2 = l2.val if l2 else 101
            
            if val1<val2 and l1!=-101:
                curr.next = ListNode(val1)
                l1=l1.next
            else:
                curr.next = ListNode(val2)
                l2=l2.next
            
            curr = curr.next
        
        
        return dummy.next
            