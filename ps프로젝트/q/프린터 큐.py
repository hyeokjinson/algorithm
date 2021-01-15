from collections import deque

if __name__ == '__main__':
    t=int(input())
    res=[]
    for _ in range(t):
        n,m=map(int,input().split())
        arr=[(key,value)for key,value in enumerate(list(map(int,input().split())))]
        q=deque(arr)
        cnt=0

        while True:
            num1=q.popleft()
            if any(num1[1]<x[1]for x in q):
                q.append(num1)
            else:
                cnt+=1
                if num1[0]==m:
                    res.append(cnt)
                    break
    for x in res:
        print(x)