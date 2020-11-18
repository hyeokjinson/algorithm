import sys

input=sys.stdin.readline


if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        number_list=[]
        for i in range(n):
            number_list.append(input().strip())

        number_list.sort()
        res=True
        for i in range(n-1):
            length=len(number_list[i])

            if number_list[i]==number_list[i+1][:length]:
                res=False
        if res:
            print("YES")
        else:
            print("NO")




