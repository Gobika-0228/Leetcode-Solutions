class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        
        // Step 1: Every child must have at least one candy
        for (int i = 0; i < n; i++) {
            candies[i] = 1;
        }
        
        // Step 2: Left-to-right pass
        // If a child has a higher rating than the left neighbor, give more
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        
        // Step 3: Right-to-left pass
        // If a child has a higher rating than the right neighbor, 
        // ensure they have more than the right neighbor.
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                // Take the max to satisfy both left and right conditions
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
            }
        }
        
        // Step 4: Sum up the total candies
        int totalCandies = 0;
        for (int candy : candies) {
            totalCandies += candy;
        }
        
        return totalCandies;
    }
}
