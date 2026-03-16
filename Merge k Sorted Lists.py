import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # 1. Put the head of each list into the heap
        for i, node in enumerate(lists):
            if node:
                # Store (value, unique_index, node_object)
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Extract the minimum and move forward
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # 3. If there's a next node in that specific list, push it
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
