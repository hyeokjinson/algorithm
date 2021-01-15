from collections import deque
if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        s=input()
        n=int(input())
        arr=input()
        arr=arr[1:-1]
        if ',' not in arr and arr!='':
            q=deque([int(arr)])
        elif arr!='':
            q=deque(map(int,arr.split(',')))
        else:
            q=deque()
        cnt=0
        flag=1
        for x in s:
            if x=='R':
                cnt+=1
            else:
                if len(q)==0:
                    flag=0
                    break
                if cnt%2==0:
                    q.popleft()
                else:
                    q.pop()
        if cnt%2==1:
            q.reverse()
        if flag:
            print('[',end='')
            for i in range(len(q)):
                if i==len(q)-1:
                    print(str(q[i]),end='')
                else:
                    print(str(q[i])+',',end='')
            print(']')
        else:
            print('error')

