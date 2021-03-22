#!/usr/bin/env python3
from z3 import Int, Real, solve, simplify, And, set_option

x = Int('x')
y = Int('y')

solve(x > 2, y < 10, x + 2*y == 7)
print(simplify(x + y + 2*x + 3))
print(simplify(x < y + x + 2))
print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))

print()

print(x**2 + y**2 >= 1)
set_option(html_mode=False)
print(x**2 + y**2 >= 1)

print()
n = x + y >= 3
print("num args: ", n.num_args())
print("children: ", n.children())
print("1st child:", n.arg(0))
print("2nd child:", n.arg(1))
print("operator: ", n.decl())
print("op name:  ", n.decl().name())


print()
x = Real('x')
y = Real('y')
solve(x**2 + y**2 > 3, x**3 + y < 5)

print()
set_option(precision=30)
print("Solving, and displaying result with 30 decimal places")
solve(x**2 + y**2 == 3, x**3 == 2)
