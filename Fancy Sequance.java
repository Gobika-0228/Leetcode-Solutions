import java.util.*;

class Fancy {
    private List<Long> nums = new ArrayList<>();
    private long a = 1, b = 0;
    private static final int MOD = 1_000_000_007;

    public Fancy() {}

    public void append(int val) {
        // Reverse transformation: (val - b) * inv(a)
        long invA = power(a, MOD - 2);
        long transformed = ((val - b + MOD) % MOD * invA) % MOD;
        nums.add(transformed);
    }

    public void addAll(int inc) {
        b = (b + inc) % MOD;
    }

    public void multAll(int m) {
        a = (a * m) % MOD;
        b = (b * m) % MOD;
    }

    public int getIndex(int idx) {
        if (idx >= nums.size()) return -1;
        // Apply current transformation: (a * stored_val) + b
        return (int) ((a * nums.get(idx) + b) % MOD);
    }

    private long power(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }
}
