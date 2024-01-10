import z3
import re

with open("input", 'r') as file:
	rhombs = [tuple(map(int, re.findall("(-?\d+)", line))) for line in file.readlines()]

x, y, z = z3.Ints("x y z")

overlaps = [z3.If(z3.Abs(x - xr) + z3.Abs(y - yr) + z3.Abs(z - zr) <= r, 1, 0) 
	for xr, yr, zr, r in rhombs]

opt = z3.Optimize()
opt.maximize(sum(overlaps))

dist = z3.Abs(x) + z3.Abs(y) + z3.Abs(z)
opt.minimize(dist)

if opt.check() != z3.sat:
	print('No solution found!')
	exit(-1)

print(opt.model().evaluate(dist))
