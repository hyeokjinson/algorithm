from itertools import permutations

def check_same(check,num):
    strike,ball=(0,0)

    for i in range(3):
        if check[i]==num[i]:
            strike+=1
        if check[i] in num:
            ball+=1
    return (strike,ball-strike)

if __name__ == '__main__':
    n=int(input())
    number=[str(i) for i in range(1,10)]
    n_list=list(map(''.join,(permutations(number,3))))
    arr=[]

    for _ in range(n):
        num,strike,ball=map(int,input().split())
        arr.append((num,strike,ball))

    for num,strike,ball in arr:
        n_list=[check for check in n_list if check_same(check,str(num))==(strike,ball)]
    print(len(n_list))