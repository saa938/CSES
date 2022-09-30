s = input().strip()
n = len(s)
ans = 0
d = 0
for i in range(1,n):
	if s[i] == s[i-1]:
		d += 1	
	else:
		ans = max(ans, d+1)
		d= 0
ans = max(ans, d+1)
print(ans)