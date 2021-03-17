from collections import deque

def solution(n,w,l,truck):
    trucks=deque(truck)
    on_bridge=deque()
    on_bridge_time=deque()

    time=0

    while on_bridge or trucks:
        time+=1

        if on_bridge:
            if on_bridge_time[0]+w==time:
                on_bridge.popleft()
                on_bridge_time.popleft()
        if trucks:
            if sum(on_bridge)+trucks[0]<=l:
                on_bridge.append(trucks.popleft())
                on_bridge_time.append(time)
    print(time)

if __name__ == '__main__':
    n,w,l=map(int,input().split())
    truck=list(map(int,input().split()))

    solution(n,w,l,truck)
