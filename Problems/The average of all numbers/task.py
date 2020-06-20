a = int(input())
b = int(input())
count = 0
add = 0
for c in range(a, b + 1):
    if c % 3 == 0:
        count += 1
        add += c

avg = add / count
print(avg)
