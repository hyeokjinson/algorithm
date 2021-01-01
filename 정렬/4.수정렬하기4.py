import sys
input=sys.stdin.readline

if __name__ == '__main__':
    arr=[]
    n=int(input())
    for _ in range(n):
        arr.append(int(input()))
    res=sorted(arr,reverse=True)
    for x in res:
        print(x)