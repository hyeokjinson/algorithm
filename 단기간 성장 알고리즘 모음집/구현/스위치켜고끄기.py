def boy(num):

    i=num

    while num-1<n:
        switch[num-1]=on_off[switch[num-1]]
        num+=i
def girl(num):
    i,j=num-2,num
    switch[num-1]=on_off[switch[num-1]]

    while i>=0 and j<n:
        if switch[i]==switch[j]:
            switch[i]=on_off[switch[i]]
            switch[j]=on_off[switch[j]]
        else:
            break
        i-=1
        j+=1

if __name__ == '__main__':
    n=int(input())
    on_off={1:0,0:1}
    switch=list(map(int,input().split()))
    student_num=int(input())

    for _ in range(student_num):
        sex,num=map(int,input().split())

        if sex==1:
            boy(num)
        elif sex==2:
            girl(num)

    for i in range(0,n,20):
        print(*switch[i:i+20])