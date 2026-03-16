class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                # Every single cell is a rhombus of size 0
                sums.add(grid[r][c])
                
                # Try expanding the rhombus size 's'
                # s is the horizontal/vertical distance from the center to a corner
                for s in range(1, 50):
                    # Define the four corners based on top corner (r, c)
                    top = (r, c)
                    right = (r + s, c + s)
                    bottom = (r + 2 * s, c)
                    left = (r + s, c - s)
                    
                    # Check if all corners are within grid boundaries
                    if not (right[0] < m and right[1] < n and 
                            bottom[0] < m and 
                            left[0] < m and left[1] >= 0):
                        break
                    
                    # Calculate border sum
                    current_sum = 0
                    # Top to Right and Bottom to Left
                    for i in range(s):
                        current_sum += grid[top[0] + i][top[1] + i]
                        current_sum += grid[bottom[0] - i][bottom[1] - i]
                    # Right to Bottom and Left to Top
                    for i in range(s):
                        current_sum += grid[right[0] + i][right[1] - i]
                        current_sum += grid[left[0] - i][left[1] + i]
                        
                    sums.add(current_sum)
        
        # Return the top 3 distinct sums in descending order
        return sorted(list(sums), reverse=True)[:3]
