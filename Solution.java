class Solution {
    static int setBits(int N) {
        // code here
        int c = 0; // counter
        while (N > 0) {
            N = N & (N - 1); // used to unset the last set bit
            c++;
        }
        return (c);
    }
}