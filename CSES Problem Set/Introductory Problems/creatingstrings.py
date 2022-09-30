s = ''.join(sorted(list(input().strip())))
n = len(s)
ans = []

char_count = [0] * 26
def search(string):
	if len(string) == n:
	
		ans.append(string)
		return
	else:
		for i in range(26):
			if char_count[i] > 0:
				char_count[i] -= 1
				search(string + chr(ord('a') + i))
				char_count[i] += 1
for i in s:
	char_count[ord(i) - ord('a')] += 1
search("")
print(len(ans))
for i in ans:
	print(i)