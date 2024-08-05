# 음식물 피하기

# 1. 아이디어
# - 2중 for문 돌면서 값이 1일때(음식물있을때) dfs활용하여 크기 구하기
# - 음식물 해당 좌표값을 1로 변환
# - dfs -> count를 전역변수로 설정 -> 4방향으로 돌때 -> 범위가 맞고 -> 값이1 
# and 방문하지x -> 방문표시o -> count += 1 -> dfs재귀탐색

# 2. 시간복잡도
# - O(V+E)
# - V = M*N
# - E = V*4

import sys
sys.setrecursionlimit(10000)
#input = sys.stdin.readline

# N:세로 M:가로 K:음식물개수
N, M, K = map(int, input().split())
# 그래프, 음식물 좌표를 1로 설정, 나머지 0
graph = [[0] * M for _ in range(N)]
for i in range(K):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
# 방문확인 그래프
chk = [[False] * M for _ in range(N)]
result = 0

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def dfs(y,x):
    global cnt
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<M:
            if graph[ny][nx]==1 and chk[ny][nx]==False:
                chk[ny][nx] = True
                cnt += 1
                dfs(ny,nx)

for j in range(N):
    for i in range(M):
        if graph[j][i]==1 and chk[j][i]==False:
            #chk[j][i] = True
            # 위의 코드처럼 방문처리후 미리 cnt를 1개로 올려서 dfs를
            # 실행하는것보다 방문처리하지 않고 cnt=0으로 두고
            # dfs가 순수하게 계산하도록 처리 -> 런타임 에러 해결
            cnt = 0
            dfs(j, i)
            result = max(result, cnt)

print(result)
            
            

