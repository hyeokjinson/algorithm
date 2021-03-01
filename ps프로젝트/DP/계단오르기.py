import sys

if __name__ == '__main__':
    n=int(input())
    arr=[0 for _ in range(301)]

    for i in range(n):
        arr[i]=int(input())

    dy=[0]*301

    dy[0]=arr[0]
    dy[1]=arr[0]+arr[1]
    dy[2]=max(arr[1]+arr[2],arr[0]+arr[2])

    for i in range(3,n):
        dy[i]=max(dy[i-2]+arr[i],dy[i-3]+arr[i-1]+arr[i])
    print(dy[n-1])