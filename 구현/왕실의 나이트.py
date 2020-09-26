input_data=input()
x=int(input_data[1])
y=int(ord(input_data[0]))-int(ord('a'))+1
steps=[(-1,-2),(1,-2),(-1,2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]

res=0
for step in steps:
    nx=x+step[0]
    ny=y+step[1]
    if 1<=nx<=8 and 1<=ny<=8:
        res+=1
print(res)