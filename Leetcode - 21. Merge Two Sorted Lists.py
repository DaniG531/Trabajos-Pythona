# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = [1,2,4]
        l2 = [1,3,4]

        A = l1+l2
        A.sort()
        B = C = ListNode()
        print(A)
        for i in A:
            B.next = ListNode(i)
            B = B.next
        return C.next