import sys
n=int(input())
num=list(map(int,input().split()))
num=list(set(num))
num.sort()
print(*num)