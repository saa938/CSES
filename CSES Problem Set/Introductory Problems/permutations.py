n = int(input())
if n == 2 or n == 3:
	print("NO SOLUTION")
else:
	ns = []
	v = 2
	while v <= n:
		ns.append(str(v))
		v += 2
	v = 1
	while v <= n:
		ns.append(str(v))
		v += 2
	print(" ".join(ns))