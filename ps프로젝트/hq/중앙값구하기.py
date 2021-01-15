import heapq
import sys

input=sys.stdin.readline
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        m=int(input())
        arr=list(map(int,input().split()))
        for j in range(m//10):
            arr.extend(list(map(int,input().split())))
        res=[]
        max_q = []
        min_q = []
        cnt=1
        for x in arr:
            if not max_q:
                heapq.heappush(max_q,-x)
            elif len(max_q)==len(min_q):
                heapq.heappush(max_q,-x)
            else:
                heapq.heappush(min_q,x)

            if max_q and min_q and -max_q[0]>=min_q[0]:
                a=heapq.heappop(max_q)
                b=heapq.heappop(min_q)

                heapq.heappush(max_q,-b)
                heapq.heappush(min_q,-a)
            if cnt%2==1:
                res.append(-max_q[0])
            cnt+=1

        print(len(res))
        flag=0
        for x in res:
            flag+=1
            print(x,end=' ')
            if flag%10==0:
                print()
        print()