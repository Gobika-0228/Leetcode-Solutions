import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, String current, int open, int close, int max) {
        // Base case: if the string is complete
        if (current.length() == max * 2) {
            result.add(current);
            return;
        }

        // Rule 1: We can always add an opening bracket if we haven't reached 'n'
        if (open < max) {
            backtrack(result, current + "(", open + 1, close, max);
        }

        // Rule 2: We can only add a closing bracket if it won't "orphan" it
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, max);
        }
    }
}
