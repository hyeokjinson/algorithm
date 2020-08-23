n,k=map(int,input().split())
coin_list=[int(input())for _ in range(n)]

cnt=0
for i in range(1,n+1):
    coin=coin_list[-i]

    if k>=coin:
        num=k//coin
        k-=num*coin
        cnt+=num

print(cnt)