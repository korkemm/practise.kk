import string

s = input().lower()
cleaned = ""

for ch in s:
    if ch.isalnum():
        cleaned += ch

print(cleaned == cleaned[::-1])