from collections import deque
import sys
def solve(k):
    if k==len(n):
        max_num=0

        for i in range(len(arr)):
            max_num=max(max_num,int(arr[i]))

        if max_num==len(arr):
            for i in range(len(arr)):
                print(int(arr[i]),end=' ')
            sys.exit(0)
        return
    if k<len(n) and int(n[k])<=50 and not visit[int(n[k])]:
        visit[int(n[k])]=1
        arr.append(n[k])
        solve(k+1)
        arr.pop()
        visit[int(n[k])]=0
    if k<len(n) and int(n[k:k+2])<=50 and not visit[int(n[k:k+2])]:
        visit[int(n[k:k+2])]=1
        arr.append(n[k:k+2])
        solve(k+2)
        arr.pop()
        visit[int(n[k:k+2])]=0

if __name__ == '__main__':
    arr=deque()
    n=input()
    visit=[0]*51
    solve(0)
