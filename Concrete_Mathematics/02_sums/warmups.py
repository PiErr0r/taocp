"""
W1

same as \Sigma_{k=0}^4 q_k
"""

"""
W2

if x > 0:
    x * (1 - 0) = x
elif x < 0:
    x * (0 - 1) = -x
x * ([x>0]-[x<0]) = abs(x)
"""

"""
W3

a_0 + a_1 + a_2 + a_3 + a_4 + a_5

a_0 + a_1 + a_4
"""

"""
W4

too much writing but I get the point

a) k is the innermost sum
b) i -||-
"""

"""
W5

the step over second equality sign is wrong

the resulting sum on the left side equals:
a_1/a_1 + a_1/a_2 + ... + a_1 / a_n +
a_2/a_1 + a_2/a_2 + ... + a_2 / a_m +
...
a_n/a_1 + a_n/a_2 + ... + a_n/a_n

and the step made in the expression assumes
a_1/a_1 + a_2/a_2 + ... + a_n/a_n +
a_1/a_1 + a_2/a_2 + ... + a_n/a_n +
...
a_1/a_1 + a_2/a_2 + ... + a_n/a_n +
"""

"""
W6

\Sigma_k [1 <= j <= k <= n] = \Sigma_{k = 1}^n \Sigma_{j = 1}^k 1 = (1) + (1 + 1) + (1 + 1 + 1) + ... + (n) = n * (n + 1) / 2

it seems that the result doesn't depend on j, or the result could be written as

\Sigma_{j = 1}^n j
"""

"""
W7

x^rm = x (x+1) (x+2) ... (x+m-1)
x^fm = x (x-1) (x-2) ... (x-m+1)

\D f(x) = f(x) - f(x - 1)
\D x^rm = x^rm - (x-1)^rm = x (x + 1) (x + 2) ... (x + m - 1) - (x - 1) x (x + 1) (x + 2) ... (x + m - 2) = x (x + 1) (x + 2) ... (x + m - 2) (x + m - 1 - x + 1) = m x^r(m-1)

"""

"""
W8

0^rm = 0 . 1 . 2 ... (m-1) = 0
"""

"""
W9

x^f(m+n) = x^fm (x - m)^fn
x^f(2+3) = x^f2 (x-2)^3 = x (x-1) . (x-2) (x-3) (x-4) = x^f5

x^r(2+3) = x (x+1) (x+2) (x+3) (x+4)
         = x^r2 (x+2)^r3

law of exponents for rising factorial power
x^r(m+n) = x^rm (x+m)^rn

x^r(3-2) = x^r3 (x + 3)^r(-2) = x (x+1) (x+2) . XXX = x => (x+3)^r(-2) = 1/[ (x+2) (x+1) ]

so the solution is
x^r(-m) = 1/[ (x-1)(x-2)(x-3)...(x-m+1) ]

"""

