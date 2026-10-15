# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1, curr2 = head, head
        index = 0
        while curr1 and curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            if nxt1 is None or nxt2 is None:
                return False
            if nxt2.next is None:
                return False
            nxt2 = nxt2.next
            if nxt1.val == nxt2.val:
                return True
            else:
                curr1 = nxt1
                index += 1
                curr2 = nxt2
        return False