# 1. BFS활용
# - 2중 for문 활용 -> 값W & 방문x -> BFS
# - BFS돌면서 모여있는 수 계산 => 전체 N^2합 구하기

# 2. 시간복잡도
# - O(V+E)
# - V = m*n
# - E = V*4

import sys
input = sys.stdin.readline

# N:가로 M:세로
N, M = map(int, input().split())
# 지도
graph = [list(input().strip())for _ in range(M)]
# 방문 확인 지도
chk = [[False] * N for _ in range(M)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
def bfs(y, x, target):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<M and 0<=nx<N:
                if graph[ny][nx]==target and chk[ny][nx]==False:
                    chk[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    return rs*rs

sum_W = 0
sum_B = 0
for j in range(M):
    for i in range(N):
        if graph[j][i] == "W" and chk[j][i] == False:
            chk[j][i] = True
            sum_W += bfs(j,i,'W')    
        elif graph[j][i] == "B" and chk[j][i] == False:
            chk[j][i] = True
            sum_B += bfs(j,i,'B')

print(sum_W, sum_B)
