s = input()
k = int(input())

n = len(s)

if n > 0:
    k = k % n
    result = s[-k:] + s[:-k] if k != 0 else s
else:
    result = s

print(result)
