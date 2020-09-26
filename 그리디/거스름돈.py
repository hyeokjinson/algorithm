n=int(input())
coin_type=[500,100,50,10]
cnt=0
for coin in coin_type:
    cnt+=n//coin
    n=n%coin
print(cnt)