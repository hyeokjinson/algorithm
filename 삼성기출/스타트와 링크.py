from itertools import combinations

if __name__ == '__main__':
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    min_=2147000000

    team=[i for i in range(n)]

    team_combination=list(combinations(team,n//2))

    for team1 in team_combination:
        team2=[x for x in team if x not in team1]
        t1_score=0
        t2_score=0
        for x,y in list(combinations(team1,2)):
            t1_score+=arr[x][y]+arr[y][x]
        for x,y in list(combinations(team2,2)):
            t2_score+=arr[x][y]+arr[y][x]
        min_=min(min_,abs(t1_score-t2_score))
    print(min_)