double myPow(double x, int n) {
    // Use long long to prevent overflow when n is INT_MIN
    long long N = n; 
    
    // Handle the negative exponent case: x^(-n) = (1/x)^n
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }
    
    double result = 1.0;
    double current_product = x;
    
    // Binary Exponentiation (O(log n) time)
    while (N > 0) {
        // If the current bit of N is set (odd number), multiply result
        if (N % 2 == 1) {
            result *= current_product;
        }
        
        // Square the base for the next power of 2
        current_product *= current_product;
        
        // Move to the next bit (halve the exponent)
        N /= 2;
    }
    
    return result;
}
