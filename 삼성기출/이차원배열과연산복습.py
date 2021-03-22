from collections import Counter

if __name__ == '__main__':
    r,c,k=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(3)]

    time=0
    r=r-1
    c=c-1

    while time<=100:
        if r<len(arr) and c<len(arr[0]) and arr[r][c]==k:
            print(time)
            break
        flag=False

        if len(arr)<len(arr[0]):
            flag=True
            arr=list(zip(*arr))

        max_len=0
        a=[]

        for x in arr:
            cnt=Counter(x)
            if cnt.get(0):
                del cnt[0]

            num_cnt=list(map(list,cnt.items()))
            num_cnt.sort(key=lambda t:(t[1],t[0]))
            a.append(list(sum(num_cnt,[]))[:100])
            max_len=max(max_len,len(a[-1]))

        for i in range(len(a)):
            if len(a[i])<max_len:
                a[i]+=[0]*(max_len-len(a[i]))
        arr=a

        if flag:
            arr=list(zip(*arr))
        time+=1

    if time>100:
        print(-1)
