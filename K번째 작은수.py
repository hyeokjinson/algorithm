T=int(input())
result=[]
cnt=0
for t in range(T):
    n,s,e,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr=arr[s-1:e]
    arr.sort()
    result.append(arr[k-1])
for i in range(len(result)):
    print("#%d %d" %(i+1,result[i]))