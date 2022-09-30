n = int(input())
nums = [str(n)]
while n != 1:
	if n % 2 == 0:
		nums.append(str(n//2))
		n //=2
	else:
		n=n*3 + 1
		nums.append(str(n))
print(" ".join(nums))