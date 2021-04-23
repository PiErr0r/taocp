# Homework
"""
Ex.8

Q(0) = a
Q(1) = b
Q(n) = (1 + Q(n - 1)) / Q(n - 2)
Q(2) = (1 + b) / a
Q(3) = (1 + a + b) / ab
Q(4) = (1 + a) / b
Q(5) = a = Q(0)
Q(6) = b = Q(1)
...

=> Q(n) = Q(n % 5) where:
Q(0) = a
Q(1) = b
Q(2) = (1 + b) / a
Q(3) = (1 + a + b) / ab
Q(4) = (1 + a) / b
"""

"""
Ex.9 TODO
"""

"""
Ex.10
>> Not sure if I would consider this a proof but it is my line of thought

Q(n) := minimum number of moves to transfer a tower of n disks from A to B while all moves must be clockwise
R(n) := minimum number of moves to transfer a tower of n disks from B to A under the same condition

Q(n) = | 0, if n = 0
       | 2 * R(n-1) + 1, if n > 0
which could be said as we need to move the nth disk from A to B
to do that we need to move n-1 disks two places clockwise (which is done in R(n-1) moves), then we do the step of the nth disk
and then to put n-1 disks on top of the nth disk which requires R(n-1) moves, hence Q(n) = 2*R(n-1)+1 moves

R(n) = | 0, if n = 0
       | Q(n) + Q(n-1) + 1, if n > 0
with the same line of reasoning as in the previous part we need to move n-1 disks two places to the right (R(n-1)) after which we can move nth disk right by one place(1)
then we move n-1 disks by one to the peg A (Q(n-1)) we are then allowed to move nth disk by one more (1) and to put the n-1 disks on top of the nth disk we need R(n-1) moves
to sum it up R(n) = R(n-1) + 1 + Q(n-1) + 1 + R(n-1) = 2*R(n-1) + 1 + Q(n-1) + 1 = Q(n) + Q(n-1) + 1 if we substitute with result from previous part of the exercise
"""

"""
Ex.11a

lets do some runt work
T(0) = 0
T(1) = 2
T(2) = 6
T(3) = 14
T(4) = 2 * T(3) + 2
prop: T(n) = 2 * T(n-1) + 2 = 2^(n+1)-2

T(0) = 0 #base for induction
T(n) = 2 * T(n-1) + 2 = 2*(2^n-2)+2 = 2^(n+1)-4+2 = 2^(n+1)-2 //QED
"""

def solve_T(n): # recursion
    return 0 if n == 0 else 2 + 2 * solve_T(n-1)

def solve_T_c(n): #closed
    return (1 << (n+1)) - 2 # or 2 ** (n+1) - 2

"""
Ex.11b

Not sure if this is the shortest way but:
T(n) = min(3 * T(n-1) + 4 , 4 * T(n-1) + 3)
it makes sense that the right one will start to grow more rapidly at some point and that point is n = 3 so:
T(0) = 0
T(n) = | 4 * T(n-1) + 3, if n < 3
       | 3 * T(n-1) + 4, if n >= 3

This maybe is a recursive solution but I do not think that I could find the closed loop
no this isnt a solution :(
TODO
"""

def solve_Tb(n):
    if n == 0:
        return 0
    elif n < 3:
        return 4 * solve_Tb(n-1) + 3
    else:
        return 3 * solve_Tb(n-1) + 4

"""
Ex.12
Ok, so generalization of 11a for k same sized disks, lets see
T(0) = 0 # who could've known
T(1) = k
T(2) = 2 * T(1) + k
...
prop: T(n) = 2 * T(n-1) + k = k * (2^n - 1)

T(0) = 0 #base
T(n) = k + 2 * T(n-1)
     = k + 2 * (k * 2^(n-1) - k)
     = k + k * 2^n - 2 * k
     = k * (2^n - 1) //QED
"""

def solve_T_g(n, k): #recursive
    return 0 if n == 0 else 2 * solve_T_g(n-1,k) + k

def solve_T_g_c(n, k): #closed
    return 0 if n == 0 else k * (2 ** n - 1)


"""
Ex.13
Boy i have no idea how to do this one
"""

"""
Ex.14a
P(1) = 2
P(2) = 4
P(3) = 8
P(4) = 2 + 2 * 6 = 14
P(5) = 6 + 8 * 2 = 22

P(0) = 0

meh, couldn't get it myself, but this guy explains it simply enough: http://www2.washjeff.edu/users/mwoltermann/Dorrie/67.pdf

all in all it is similar to the lines problem
lets say you have n lines and you draw n + 1st line, it will be cut by all of the n lines which means it divides n regions into 2
so P(n) = P(n-1) + n

in 3D problem you have n planes and draw n+1st plane so that n planes cut it and create n lines on that plane
each of those lines divides a 3D region into 2 so R(n) = R(n-1) + P(n-1)
"""

"""
Ex.15
I see somewhat of a pattern but I can't express it mathematically
for i in range(3, 60):
    a = [j+1 for j in range(i)]
    j = 0
    while len(a) > 2:
        a.pop((j+1)%len(a))
        if j == len(a):
            j = 0
        else:
            j = (j+1)%len(a)
    print(i, (b:=a.pop(j)), a[0])
    print(bin(i)[2:], bin(b)[2:], bin(a[0])[2:])
"""

"""
Ex.16
g(1) = a
g(2n+j) = 3*g(n) + cn + bj

g(2) = 3*g(1)+cn+b0 = 3a + cn + b0
g(3) = 3a+cn+b1
g(4) = 3*g(2)+cn+b0 = 9a + 3cn + 3b0 + cn + b0 = 9a + 4cn + 4b0
g(5) = 9a+4cn+4b1
g(6) = 27a+13cn+13b0
g(7) = 27a+13cn+13b1
g(8) = 81a+40cn+40b0
[x/2] == floor(x/2)
g(n) = 3^[n/2] * a + (3^[n/2]-1)/2 * cn + (3^[n/2]-1)/2 * b[n mod 2]
"""





















