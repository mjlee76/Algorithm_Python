# 1. 아이디어
# - 2중 for문, 값 1 && 방문X => 그래프탐색 시작
# - DFS를 통해 찾은 값을 저장 후 정렬해서 출력

# 2. 시간복잡도
# - DFS : O(V+E)
# - V, E : N^2, 4N^2
# - V+E : 5N^2 ~= N^2 ~= 625 >> 2억보다 낮은값이라 가능

# 3. 자료구조
# - 그래프 저장 : int[][]
# - 방문여부 : bool[][]
# - 결과값 : int[]

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if graph[ny][nx] == 1 and chk[ny][nx] == False:
                # 방문 체크 표시
                chk[ny][nx] = True
                # DFS를 위한 재귀함수 호출
                #print(each)
                dfs(ny, nx)

for j in range(n):
    for i in range(n):
        if graph[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True
            # DFS로 크기 구하기(each 사용:전역변수)
            each = 0
            dfs(j,i)
            # 크기를 결과 리스트에 넣기 
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)