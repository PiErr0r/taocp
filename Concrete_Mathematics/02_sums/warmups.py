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


"""
