# put your python code here
class1 = int(input())
class2 = int(input())
class3 = int(input())

class1_desk = class1 // 2 + (class1 % 2)
class2_desk = class2 // 2 + (class2 % 2)
class3_desk = class3 // 2 + (class3 % 2)

required_min_desks_float = (class1_desk + class2_desk + class3_desk)
required_min_desks = int(required_min_desks_float)
print(required_min_desks)
