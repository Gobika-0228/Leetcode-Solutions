class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Check if there are at least k nodes left
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
            
        # 2. Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 3. Recurse for the next group
        # 'head' is now the tail of the reversed group
        # 'prev' is the new head of the reversed group
        if head:
            head.next = self.reverseKGroup(curr, k)
            
        return prev
