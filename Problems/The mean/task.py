l_list = []
while True:
    user_input = input()
    if user_input == '.':
        break
    l_list.append(int(user_input))

print(sum(l_list)/len(l_list))
