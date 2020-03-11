import sys

input_data=list(input())
answer=0
stack=[]

for i in range(len(input_data)):
    if input_data[i]=="(":
        stack.append("(")
    else:
        if input_data[i-1]=="(":
            stack.pop()
            answer+=len(stack)
        else:
            stack.pop()
            answer+=1
print(answer)