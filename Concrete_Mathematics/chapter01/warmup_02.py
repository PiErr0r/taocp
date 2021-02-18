"""
Warmup 2

Inductive proof
we need to move disk n two places and we have to move n-1 disks on top to the far right to allow disk n to make a move
    then we have to return n-1 disks to the far left position to create space for disk n to make another move and
    then we return n-1 disks on top of disk n
T(n) = 2 + 3 * T(n - 1)

Proposition:
    T(n) = 3^n - 1

    Trivial first step:
    T(0) = 3^0 - 1 = 1 - 1 = 0
    T(n) = 2 + 3 * T(n - 1)
         = 2 + 3 * (3 ^ (n - 1) - 1 )
         = 2 + 3^n - 3 = 3^n - 1 //QED
"""

def solve_01(n): # recurrence solution
    if (n == 0): return 0
    return 2 + 3 * solve(n-1)

def solve_c_01(n): #closed solution
    return 3 ** n - 1

"""
Warmup 3
From the recurrence relation it is proposed that each smaller disk will travel to the far right side, return to the far left and go bak again to the far right
That being said for each step bigger disk makes each smaller one will cover all of the possible configuration of disks
"""

"""
Warmup 4
Not that I can think of
"""

"""
Warmup 5
No.
Opposite circles cannot be isolated as a single group
"""

"""
Warmup 6
R(n) = 0 for n < 3
R(n) = 1 for n = 3
and the same logic applies as in the original problem because we can look at the bounded region as an unbounded infinite one since the line displacements can be infinitesimal
so
R(n) = L(n-3) for n > 3
"""

"""
Warmup 7
J(1) = 1
J(2n) = 2J(n) - 1
J(2n + 1) = 2J(n) + 1

// TODO:
"""
