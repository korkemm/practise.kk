n = int(input())
num_str = str(n)
power = len(num_str)

total = 0

for digit in num_str:
    total += int(digit) ** power

print(total == n)