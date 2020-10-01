import heapq as pq
n=int(input())
#힙에 초기 카드 묶음을 모두 삽입
heap=[]
for _ in range(n):
    data=int(input())
    pq.heappush(heap,data)
res=0
#힙에 원소가 1개 남을때 까지
while len(heap)!=1:
    #가장 작은 2개의 카드 묶음 꺼내기
    one=pq.heappop(heap)
    two=pq.heappop(heap)
    #카드 묶음을 합쳐서 다시 삽입
    sum_value=one+two
    res+=sum_value
    pq.heappush(heap,sum_value)
print(res)