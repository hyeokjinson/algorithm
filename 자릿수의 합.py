def digit_sum(x):

    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    # for i in str(x):
        # sum+=int(i)
    return sum

n=int(input())
arr=list(map(int,input().split()))
max=-10000000
for x in arr:
    total=digit_sum(x)
    if total>max:
        max=total
        score=x
print(score)