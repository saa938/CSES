n = int(input())
mod = 1000000007
ans = 1
for i in range(n):
	ans *= 2
	ans %= mod
print(ans)