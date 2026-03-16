class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the predecessor of the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # We need at least two nodes ahead of 'current' to perform a swap
        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Step 1: Point current to the second node
            current.next = second
            
            # Step 2: Fix the bridge to the rest of the list
            first.next = second.next
            
            # Step 3: Complete the swap by pointing second back to first
            second.next = first
            
            # Step 4: Move 'current' two steps forward (to the end of the swapped pair)
            current = first
            
        return dummy.next
