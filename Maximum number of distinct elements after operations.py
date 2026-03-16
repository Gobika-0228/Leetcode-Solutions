class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        # Track the value assigned to the previous element
        last_val = float('-inf')
        distinct_count = 0
        
        for x in nums:
            # We want to pick the smallest possible value > last_val
            # that is also within the range [x - k, x + k]
            candidate = max(x - k, last_val + 1)
            
            # Check if this candidate is within the allowed upper bound
            if candidate <= x + k:
                last_val = candidate
                distinct_count += 1
                
        return distinct_count
