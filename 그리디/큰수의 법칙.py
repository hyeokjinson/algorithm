n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort(reverse=True)
top1=data[0]
top2=data[1]
sum_=0
while True:
    if m==0:
        break
    for i in range(k):
      sum_+=top1
      m-=1
      if m==0:
          break
    sum_+=top2
    m-=1
print(sum_)