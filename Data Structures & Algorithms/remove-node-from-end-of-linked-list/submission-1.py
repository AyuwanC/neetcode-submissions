# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if length == 1:
            head = None
        elif length == 2:
            if n == 1:
                head.next = None
            elif n == 2:
                head = head.next
        elif length == n:
            head = head.next
        else:
            curr, nxtnxt = head, head.next.next
            for i in range(length - n - 1):
                curr = curr.next
                nxtnxt = nxtnxt.next
            print(curr.val)
            removal = curr.next
            removal.next = None
            curr.next = nxtnxt
        return head

        
        
        