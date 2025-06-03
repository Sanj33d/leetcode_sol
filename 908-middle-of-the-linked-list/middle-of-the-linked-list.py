# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = cur2 = head
        idx1 = idx2 = 0
        # if num of nodes = odd or even
        ## floor divide it then add 1
        while cur1 != None:
            idx1 += 1
            cur1 = cur1.next
        mid = (idx1//2) + 1

        while cur2 != None:
            idx2 += 1
            if idx2 == mid:
                return cur2
            cur2 = cur2.next

        
        