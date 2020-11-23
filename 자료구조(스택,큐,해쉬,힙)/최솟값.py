import heapq
import sys
from math import *

input=sys.stdin.readline

def init(node,start,end):
    if start==end:
        tree_min[node]=arr[start]
        return tree_min[node]

    mid=(start+end)//2
    tree_min[node]=min(init(node*2,start,mid),init(node*2+1,mid+1,end))
    return tree_min[node]

def query(node,start,end,left,right):
    if start>right or end<left:
        return 1000000001

    if left<=start and end<=right:
        return tree_min[node]

    mid=(start+end)//2
    return min(query(node*2,start,mid,left,right),query(node*2+1,mid+1,end,left,right))

if __name__ == '__main__':
    n,m=map(int,input().split())
    h=int(ceil(log2(n)))
    tree_size=1<<(h+1)

    arr=[]
    tree_min=[0]*tree_size

    for _ in range(n):
        arr.append(int(input()))

    init(1,0,n-1)


    for _ in range(m):
        a,b=map(int,input().split())
        print(query(1,0,n-1,a-1,b-1))
