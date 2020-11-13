def check1(a,b):
    while b:
        a,b=b,a%b
    return a
def check2(a,b):
    return a*b//check1(a,b)

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        a,b=map(int,input().split())
        print(check2(a,b))