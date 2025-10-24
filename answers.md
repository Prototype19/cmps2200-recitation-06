# CMPS 2200 Recitation 06
## Answers

**Name:** Daron Lebaredian


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

Recurrence Relation:\
W(n) = W(n-1) + W(n-2) + 1\
W(0) = W(1) = 1\

Solving Recurrence Relation:\
Define A(n) = W(n) + 1 to remove '+ 1'\
A(n) = (W(n-1) + (W(n-2) + 1) + 1\
A(n) = (W(n-1) + 1) + (W(n-2) + 1)\
A(n) = A(n-1) + A(n-2)\
A(0) = W(0) + 1 = 1 + 1 = 2\
A(1) = W(1) + 1 = 1 + 1 = 2\
Since A(n) is just the same definition as the fibonaci sequence, Solve this general solution\
A(n) = $a$$F_n+1$ + $b$$F_n$\
Substute in n = 1 and n = 2:\
n = 0: A(0) = 2 = $a$$F_n+1$ + $b$$F_n$ = $a$*1 + $b$*0 → $a$ = 2\
n = 1: A(1) = 2 = $a$$F_n+1$ + $b$$F_n$ = 2*1 + $b$*1 → $b$ = 0\
So A(n) = 2$F_n+1$
Therefore W(n) = A(n) - 1 = 2$F_n+1$ - 1

Using binet's formula we know:

$W(n) \in O(2^n)$



- **3)**

Recurrence Relation:\
S(n) = max(S(n-1) + S(n-2)) + 1\
S(0) = S(1) = 1\

Solving Recurrence Relation:\
Since we know S(n-1) will always be larger than s(n-2)\
so S(n) = S(n-1)+ 1\
Since this recurrence relatiion is balanced (each level of the expanded tree is equal) we can say:\

$S(n) \in O(n)$

- **4)**

This is the count list, each element n-1 corresponding of the frequency of calls for a f(n):\
[34, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]\

You will notice f(1) gets called more than f(0) and f(0) and f(2) get called an equal amount of times\
In general you will see that the lower number n calls gets called a lot of times while the higher number n calls gets called less.


- **6)**

- **8)**
