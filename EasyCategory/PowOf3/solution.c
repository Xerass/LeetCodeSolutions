bool isPowerOfThree(int n) {
 const int MAX_POW = 1162261467;
 return n > 0 && (MAX_POW % n == 0);
}
