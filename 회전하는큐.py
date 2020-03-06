import sys
from _collections import deque

n, _=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
queue=deque(range(1,n+1))

total_compute=0

for j in range(len(numbers)):
    if numbers[j]==queue[0]:
        queue.popleft()
        continue
    queue_idx=queue.index(numbers[j])

    if queue_idx>len(queue)//2:
        queue.rotate(len(queue)-queue_idx)
        total_compute+=(len(queue)-queue_idx)
    elif queue_idx<len(queue)//2:
        queue.rotate(-queue_idx)
        total_compute+=queue_idx
    queue.popleft()

print(total_compute)