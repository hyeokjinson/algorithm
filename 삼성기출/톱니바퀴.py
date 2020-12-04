import sys
from _collections import deque

def left(num,direction):
    if num<0:
        return
    if arr[num][2]!=arr[num+1][6]:
        left(num-1,-direction)
        arr[num].rotate(direction)

def right(num,direction):
    if num>3:
        return
    if arr[num][6]!=arr[num-1][2]:
        right(num+1,-direction)
        arr[num].rotate(direction)

if __name__ == '__main__':
    arr=[]
    for _ in range(4):
        arr.append(deque(list(input())))
    k=int(input())
    for _ in range(k):
        num,loc=map(int,input().split())
        num-=1
        left(num-1,-loc)
        right(num+1,-loc)
        arr[num].rotate(loc)
    res=0
    if arr[0][0]=='1':
        res+=1
    if arr[1][0]=='1':
        res+=2
    if arr[2][0]=='1':
        res+=4
    if arr[3][0]=='1':
        res+=8
    print(res)