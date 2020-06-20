# inp = "Kitten 10"
# print(inp)
# values = inp.split(' ')
count = 0
name = []
capacity = []
values = []
while True:
    user_ip = input()
    if user_ip == 'MEOW':
        break
    values = user_ip.split(' ')
    #    print(values)
    name.append(values[0])
    num_convert = int(values[1])
    capacity.append(num_convert)
#    print(name)
#    print(capacity)
# values.split(' ')
max_capacity = max(capacity)
# print(max_capacity)
for i in capacity:
    # print(i)
    if max_capacity == i:
        print(name[count])
    # print(capacity[count])
    else:
        # print(count, "before")
        count += 1
        # print(count, "after")
        # print("check logic")
