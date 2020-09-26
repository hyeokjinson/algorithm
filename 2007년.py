arr=[31,28,31,30,31,30,31,31,30,31,30,31]
week=["MON","TUE","WED","THU","FRI","SAT","SUN"]
day=0
x,y=map(int,input().split())
for i in range(x-1):
    day=day+arr[i]

day=(day+y)%7
print(week[day-1])