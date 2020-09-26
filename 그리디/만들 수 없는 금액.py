n=int(input())
num=list(map(int,input().split()))  #리스트 선언
total=1
num.sort() #리스트 정렬 3 2 1 1 9-> 1 1 2 3 9
for x in num:
    if total<x:                 #1을 만들수 있는지 차례로 확인
        break
    total+=x
print(total)