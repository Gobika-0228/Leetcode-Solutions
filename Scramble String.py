class Solution:
    memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # Check memo to avoid redundant calculations
        state = (s1, s2)
        if state in self.memo:
            return self.memo[state]
        
        # Base cases
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        for i in range(1, n):
            # Case 1: Substrings are NOT swapped
            if (self.isScramble(s1[:i], s2[:i]) and 
                self.isScramble(s1[i:], s2[i:])):
                self.memo[state] = True
                return True
            
            # Case 2: Substrings ARE swapped
            # s1's prefix matches s2's suffix, and s1's suffix matches s2's prefix
            if (self.isScramble(s1[:i], s2[n-i:]) and 
                self.isScramble(s1[i:], s2[:n-i])):
                self.memo[state] = True
                return True
        
        self.memo[state] = False
        return False
