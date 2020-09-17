import sys
from _collections import deque

def left(start,dirs):
    if start<0 or arr[start][2]==arr[start+1][6]:
        return
    if arr[start-1][2]!=arr[start][6]:
        left(start-1,-dirs)
        arr[start].rotate(dirs)
def right(start,dirs):
    if start>3:
        return
    if arr[start][6]!=arr[start-1][2]:
        right(start+1,-dirs)
        arr[start].rotate(dirs)


if __name__=="__main__":
    arr=[list(map(int,input().strip()))for _ in range(4)]
    k=int(input())
    arr=deque(arr)
    res=0
    for _ in range(k):
        num,sight=map(int,input().split())
        left(num-2,-sight)
        right(num,-sight)
        arr[num-1].rotate(sight)


    if arr[0][0]==1:
        res+=1
    if arr[1][0]==1:
        res+=2
    if arr[2][0]==1:
        res+=4
    if arr[3][0]==1:
        res+=8
    print(res)
