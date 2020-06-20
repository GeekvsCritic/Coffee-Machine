# put your python code here
cinema_halls = int(input())  # 9
each_hall = int(input())  # 68
total_viewers = int(input())  # 586
if total_viewers <= cinema_halls * each_hall:
    print(True)
else:
    print(False)
