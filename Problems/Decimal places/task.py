num = float(input())
deci = int(input())
cal = f"%.{deci}f"
print(f'{cal}' % (num))
# print(f'{num:.{deci}f}')
