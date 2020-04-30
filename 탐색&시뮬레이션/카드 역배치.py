arr=[i for i in range(21)]

for _ in range(10):
    a,b=map(int,input().split())
    for t in range((b-a+1)//2):
        arr[a+t],arr[b-t]=arr[b-t],arr[a+t]

print(arr[1:21])

