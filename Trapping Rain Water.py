class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        water = 0
        
        while l < r:
            # We always process the side with the lower "max" wall
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                # Water trapped is the diff between the max wall and current floor
                water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                
        return water
