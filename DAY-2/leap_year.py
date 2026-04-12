yr=int(input("enter year:"))
if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
    print(yr,'is leap year')
else:
    print('not leap year')