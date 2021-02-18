

def solve(n): # recurrence solution
    if (n == 0): return 0
    return 2 + 3 * solve(n-1)

def solve_c(n): #closed solution
    return 3 ** n - 1

"""
Inductive proof
T(n) = 2 + 3 * T(n - 1)

Proposition:
    T(n) = 3^n - 1

    Trivial first step:
    T(0) = 3^0 - 1 = 1 - 1 = 0
    T(n) = 2 + 3 * T(n - 1)
         = 2 + 3 * (3 ^ (n - 1) - 1 )
         = 2 + 3^n - 3 = 3^n - 1 //QED
"""

for i in range(20):
    print(solve(i), solve_c(i))
