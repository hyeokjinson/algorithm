import sys
from _collections import deque

n,k=map(int,sys.stdin.readline().split())
problem_output=[]
problem_input=deque(int(i+1)for i in range(n))
joinText=","
while len(problem_input)!=0:
    problem_input.rotate(-k+1)
    problem_output.append(str(problem_input.popleft()))
print("<"+joinText.join(problem_output)+">")