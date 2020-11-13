#세그먼트 트리 생성
def init(node,start,end):
    #node가 leaf 노드인 경우 배열의 원소값을 반환
    if start==end:
        tree[node]=l[start]
        return tree[node]
    else:
        tree[node]=init(node*2,start,(start+end)//2+init(node*2+1,(s)))


if __name__ == '__main__':
    n,m,k=map(int,input().split())
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
