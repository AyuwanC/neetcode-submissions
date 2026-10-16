class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        n = len(stack)
        curr = head

        for i in range(n // 2):
            nxt = curr.next
            popped = stack.pop()

            curr.next = popped
            popped.next = nxt

            curr = nxt

        curr.next = None