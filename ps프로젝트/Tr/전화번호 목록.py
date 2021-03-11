import sys

input=sys.stdin.readline

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        num_list=[]
        for i in range(n):
            num_list.append(input().strip())

        num_list.sort()
        flag=False
        for i in range(n-1):
            length=len(num_list[i])
            if num_list[i]==num_list[i+1][:length]:
                flag=True
        if flag:
            print("NO")
        else:
            print("YES")