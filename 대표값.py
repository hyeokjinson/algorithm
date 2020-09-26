n=int(input())
a=list(map(int,input().split()))
result=round(sum(a)/n) #round :소수첫째자리에서 반올림
min=2147000000
for idx,x in enumerate(a):
    tmp=abs(x-result)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(result,res)