n, m, tolerance = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))
applicants.sort()
apartments.sort()

ans,i,j=0,0,0
while i < n and j < m:
	applicant = applicants[i]
	apartment = apartments[j]
	if apartment < applicant - tolerance:
		j += 1
	elif apartment > applicant + tolerance:
		i += 1
	else:
		ans+=1
		i+=1
		j+=1
print(ans)
