from _collections import deque

arr=list("A man, a plan, a canal - Panama")
des=deque()

for val in arr:
    if val.isalpha():
        des.append(val)

cnt=int(len(des)/2)

for x in range(cnt):
    if des.popleft().lower() !=des.pop().lower():
        print("회문이 아니다")
        exit(0)
print("회문이지롱")
