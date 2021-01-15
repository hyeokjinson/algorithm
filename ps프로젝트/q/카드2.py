from collections import deque

if __name__ == '__main__':

    n=int(input())
    q=deque(range(1,n+1))

    while len(q)>1:
        q.popleft()
        tmp=q.popleft()
        q.append(tmp)
    print(q[0])