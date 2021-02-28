import sys

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    arr.insert(0,0)

    dy=[0]*(n+1)

    if n==1:
        print(1)
        sys.exit(0)

    for i in range(1,n+1):
        dy[i]=1
        for j in range(i):
            if arr[i]<arr[j]:
                dy[i]=max(dy[i],dy[j]+1)
    print(max(dy))