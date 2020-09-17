def sol():
    global res
    for i in range(n):
        if a[i]>0:
            a[i]-=b
            res+=1
        if a[i]>0:
            res+=a[i]//c
            if a[i]%c!=0:
                res+=1


n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
res=0
sol()
print(res)