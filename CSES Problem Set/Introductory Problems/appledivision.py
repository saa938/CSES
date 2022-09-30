n = int(input())
a = list(map(int, input().split()))

def s(i, wa, wb):
	if i == n:
		return abs(wa-wb)
	pa=s(i+1, wa+a[i], wb)
	pb = s(i+1, wa, wb+a[i])
	return min(pa,pb)
print(s(0,0,0))
