import sys
input=sys.stdin.readline

def width():
    global res

    for i in range(n):
        tmp=1
        for j in range(1,n):
            if arr[i][j]==arr[i][j-1]:
                tmp+=1
            else:
                if res<tmp:
                    res=tmp
                tmp=1

        if res<tmp:
            res=tmp

def height():
    global res

    for i in range(n):
        tmp=1
        for j in range(1,n):
            if arr[j][i]==arr[j-1][i]:
                tmp+=1
            else:
                if res<tmp:
                    res=tmp
                tmp=1

        if res<tmp:
            res=tmp

if __name__ == '__main__':
    n=int(input())
    arr=[list(input())for _ in range(n)]
    res=-2147000000

    for i in range(n):
        for j in range(1,n):
            arr[i][j],arr[i][j-1]=arr[i][j-1],arr[i][j]
            width()
            height()
            arr[i][j],arr[i][j-1]=arr[i][j-1],arr[i][j]

    for i in range(n):
        for j in range(1,n):
            arr[j][i],arr[j-1][i]=arr[j-1][i],arr[j][i]
            width()
            height()
            arr[j][i],arr[j-1][i]=arr[j-1][i],arr[j][i]

    print(res)