import sys
n=int(input())
num=list(map(int,input().split()))
a_value=0
b_value=0
max_value=max(num)

res1=set()

if len(num)==1:
    print('A')
    sys.exit(0)
elif len(num)==2:
    if num[0]==num[1]:
        print(num[0])
        sys.exit(0)
    else:
        print('B')
        sys.exit(0)

for i in range(n-1):
    for a in range(50):
        for b in range(50):
            if num[i]*a+b==num[i+1]:
                a_value=a
                b_value=b
                res1.add((a_value,b_value))
                break
res=0
for a,b in res1:
    cnt = 0
    for i in range(n-1):
        if num[i]*a+b==num[i+1]:
            cnt+=1
    if cnt==n-1:
        res+=1
        a_value=a
        b_value=b


print(num[-1] * a_value + b_value)