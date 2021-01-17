import sys

input=sys.stdin.readline

if __name__ == '__main__':
    a,p=map(int,input().split())
    arr=[a]

    while True:
        res=0
        for x in str(arr[-1]):
            res+=int(x)**p
        if res in arr:
            idx=arr.index(res)
            print(len(arr[:idx]))
            break
        else:
            arr.append(res)