def num1(x):
    cnt=0
    for i in range(1,x+1):
        if x%i==0:
            cnt+=1
    return cnt
res=0
s=input()
for x in s:
    if x.isdecimal():      
        res=res*10+int(x)
num=num1(res)
print(res)
print(num)