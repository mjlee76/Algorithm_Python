# 1.아이디어
# - 정점간의 연결된 정보를 2차원 배열에 저장
# - 방문확인을 해줄 리스트 선언(각 1개씩 총 2개)
# - bfs 를 이용하여 큐가 빌때까지 다음행동 진행
#     - 방문표시, 큐를 pop, pop한 값 출력
#     - for문을 돌면서 방문하지 않은곳이고 pop한 정점과 연결된 값이 1이라면
#     - 해당 정점을 큐에 append
# - dfs 를 이용하여 탐색시 다음행동 진행
#     - 첫 정점을 방문표시 후 출력
#     - for문을 돌면서 방문하지 않은곳이고 pop한 정점과 연결된 값이 1이라면
#     - 재귀함수 실행

import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

chk_bfs = [False] * (N+1)
chk_dfs = chk_bfs.copy()

def bfs(V):
    q = [V]
    chk_bfs[V] = True
    while q:
        V = q.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and chk_bfs[i] == False:
                q.append(i)
                chk_bfs[i] = True
                

def dfs(V):
    chk_dfs[V] = True
    print(V, end = ' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and chk_dfs[i] == False:
            dfs(i)  
            
dfs(V)
print()
bfs(V)