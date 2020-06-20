"""
n = int(input())  # number of values
for _ in range(n):
    ip = int(input())
    if ip % 7 == 0:
        print(ip ** 2)

"""

n = int(input())  # number of values
ip = []
for _ in range(n):
    ip.append(int(input()))

for i in ip:
    if i % 7 == 0:
        print(i ** 2)
