n = int(input())
num = list(map(int, input().split()))
ans = 0
for i in range(1,n):
	if num[i] < num[i-1]:
		ans += num[i-1] - num[i]
		num[i] = num[i-1]
print(ans)