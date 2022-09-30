n, weight = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
hgondolas = []
for i in range(n):
	hgondolas.append(False)
gondolas = 0
w = 0
j,i=n-1,0
while i < j:
	if weights[i] + weights[j] > weight:
		j -= 1
	else:
		gondolas += 1
		hgondolas[i],hgondolas[j]=True,True
		i += 1
		j -= 1
for i in hgondolas:
	if not i:
		gondolas += 1
print(gondolas)