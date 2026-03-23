class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # While the current number is in range [1, n] and not in its correct spot
            # (e.g., the value 3 belongs at index 2)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap it to its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # First index where the value doesn't match the (index + 1) is our missing number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers 1 to n are present, the missing one is n + 1
        return n + 1
