class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        long totalSum = 0;

        // Step 1: Calculate the total sum of the grid
        for (int[] row : grid) {
            for (int val : row) {
                totalSum += val;
            }
        }

        // If the total sum is odd, we can't split it into two equal integer sums
        if (totalSum % 2 != 0) return false;
        long target = totalSum / 2;

        // Step 2: Check horizontal cuts
        long currentHorizontalSum = 0;
        for (int i = 0; i < m - 1; i++) { // m-1 to ensure non-empty sections
            for (int j = 0; j < n; j++) {
                currentHorizontalSum += grid[i][j];
            }
            if (currentHorizontalSum == target) return true;
            if (currentHorizontalSum > target) break; // Optimization: sums only increase
        }

        // Step 3: Check vertical cuts
        long currentVerticalSum = 0;
        for (int j = 0; j < n - 1; j++) { // n-1 to ensure non-empty sections
            for (int i = 0; i < m; i++) {
                currentVerticalSum += grid[i][j];
            }
            if (currentVerticalSum == target) return true;
            if (currentVerticalSum > target) break;
        }

        return false;
    }
}
