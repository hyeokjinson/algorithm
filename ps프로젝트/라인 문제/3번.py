from collections import deque

def solution(enter, leave):
    answer = [0]*len(enter)
    enter=deque(enter)
    leave=deque(leave)
    stack=[]
    for i in range(len(enter)):
        if enter[i]==leave[i]:
            enter.popleft()
        elif enter[i] in stack:
            while True:
                if enter[i]==stack[0]:
                    stack.pop(0)
                    break
                else:


        else:
            stack.append(enter[i])

    return answer

enter=[1,3,2]
leave=[1,2,3]
print(solution(enter,leave))