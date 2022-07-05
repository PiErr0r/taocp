# Basics

## B11

```
S (0 <= k < n) [ (a_(k+1) - a_k) b_k ] = a_n b_n - a_0 b_0 - S (0 <= k < n) [ a_(k+1) (b_(k+1) - b_k) ]
= b0 (a1 - a0) + b1 (a2 - a1) + b2 (a3 - a2) + ... + b_(n-1) (a_n - a_(n-1))
= b0 a1 - b0 a0 + b1 a2 - b1 a1 + ... + b_(n-1) a_n - b_(n-1) a_(n-1) + [a_n b_n - a_n b_n]
= a_n b_n - a0 b0 + a1(b0 - b1) + a2(b1 - b2) + a_n (b_(n-1) - b_n)
= a_n b_n - a0 b0 + S(0 <= k < n) [ a_(k+1) (b_k - b_(k+1)) ]
= a_n b_n - a0 b0 - S(0 <= k < n) [ a_(k+1) (b_(k+1) - b_k) ]
```


