from itertools import chain
def solution(n):
    arr=[[0 for _ in range(n)]for _ in range(n)]
    y,x=-1,0
    number=1

    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                y+=1
            elif i%3==1:
                x+=1
            elif i%3==2:
                y-=1
                x-=1
            arr[y][x]=number
            number+=1
    print(arr)
    res=[i for i in chain(*arr) if i!=0]
    return res
if __name__ == '__main__':
    solution(4)