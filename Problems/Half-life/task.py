num = int(input())
reduction = int(input())
time = 12
half_life = num // 2
count = 1
while half_life > reduction:
    half_life = half_life // 2
    count += 1
print(count * 12)
