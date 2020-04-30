n=int(input())
arr=list(map(int,input().split()))

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x = x // 10
    return res
for x in arr:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp,end=' ')