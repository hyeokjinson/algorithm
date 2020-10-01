n=int(input())
arr=[list(map(str,input().split()))for _ in range(n)]
arr.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for x in arr:
    print(x[0])